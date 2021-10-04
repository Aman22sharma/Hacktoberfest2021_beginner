import smtplib 
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()


sender = input('enter your email')
password = input('enter your password')
message = input('enter your message)

recivers = ['enter recivers email']

a = smtplib.SMTP('smtp.gmail.com',587)

a.starttls()

msg['Subject'] = "hii this is mail"

a.login('sender','password')

a.sendmail('sender',recivers,'test message')

a.quit()


