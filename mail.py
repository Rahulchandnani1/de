

import smtplib
import urllib.request as urllib
# Senders email
sender_email = "tnamaste370@gmail.com"
# Receivers email
receiveremail = "tnamaste573@gmail.com"
message ="Best Model is being created... Thank You"
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login("tnamaste370@gmail.com", "")
print("Login Success!")

server.sendmail("Rahul chandnani", "tnamaste573@gmail.com", message)
print(f"Email has been sent successfully to {rec_email}")




