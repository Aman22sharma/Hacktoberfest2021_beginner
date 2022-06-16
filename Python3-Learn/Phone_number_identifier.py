#pip install phonenumbers
import phonenumbers
from phonenumbers import carrier,geocoder,timezone

#Enter the number
mobileNo = input("Enter the mobile no. with country code: ")
mobileNo = phonenumbers.parse(mobileNo)

# getting the timezone of the number
print(timezone.time_zones_for_number(mobileNo))

#getting carrier of number(service provider)
print(carrier.name_for_number(mobileNo, "en"))

#getting the regional information
print(geocoder.description_for_number(mobileNo,"en"))

#check validation
print(phonenumbers.is_valid_number(mobileNo))

#check possibility
print(phonenumbers.is_possible_number(mobileNo))