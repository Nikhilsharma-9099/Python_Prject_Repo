from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = "niksharma907@gmail.com"
email_password = password

email_reciever = "cenabe9466@lewenbo.com"

subject = "Don't forget to subscribe"

body = """
   When you watch a video, kindly hit subscribe
   """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())