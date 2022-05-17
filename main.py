import smtplib
import ssl
from email.message import EmailMessage

subject = "Email"
body = "test email"
to_email = "sandraedcba@gmail.com"
from_email = "sandraedcba@gmail.com"
password = input("enter a password: ")


message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["subject"] = subject
message.set_content(body)

context = ssl.create_default_context()
print("Sending email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_email, password)
    server.sendmail(from_email, to_email,message.as_string())
print("email sent")