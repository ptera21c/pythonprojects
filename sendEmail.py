import smtplib
import ssl
from email.message import EmailMessage

sender_email = input("Enter your email: ")
password = input("Enter your password: ")

subject = input("Enter the subject of your email: ")

body = input("Enter the body of your email: ")


receiver_email = input("Enter the receiver email: ")


message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)



context = ssl.create_default_context()

print("sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("email sent!")
