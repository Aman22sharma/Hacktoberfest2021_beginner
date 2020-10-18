import argparse
import requests
import json

parser= argparse.ArgumentParse()

parser.add_argument("-i", "--ipaddress", help="track IP address")

args= parser.parse_args()

ip= args.ipaddress

url="http://ip-api.com/json"+ ip

response= requests.get(url)
data= json.loads(response)
print(data.content)