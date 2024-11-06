# Send Email to Anyone using just Receiver Email Id in Python !!
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'divyakantdabhi1609@gmail.com'
email_password = 'lpph qjvq wedr rouy'
email_receiver = ''

# for getting email_password !! You need to Go to your Gmail Account !!
# Open this URL Link : https://myaccount.google.com/apppasswords
# Create a password with App Name : Python

subject = "Testing Email using Python !!"
body = "Succeed testing Python Email"

if not email_receiver:
    print("Enter Receiver Email ID !!")
    exit()

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        print("Login Success!!")
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Email sent success!!")
except smtplib.SMTPException as e:
    print("Failed to send email. Error:", str(e))
except Exception as e:
    print("An unexpected error occurred:", str(e))
