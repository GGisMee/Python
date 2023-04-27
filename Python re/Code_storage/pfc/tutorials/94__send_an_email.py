# 94__send_an_email

# funkar inte pga uppdaterade mail skyddningskrav

import smtplib # simple mail transfer protocol library

sender = "ggamstedt@gmail.com"
receiver = "gustav.gamstedt@outlook.com"
password = "No"
subject = "Test email" # to python
body = "This is a test preformed on python"

# header
message = f"""
From: Gustav {sender} 
To {receiver}
Subject: {subject}\n
{body}
"""
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    print("Logged in...")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")

try:
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
except smtplib.SMTPSenderRefused:
    print("Auth required")