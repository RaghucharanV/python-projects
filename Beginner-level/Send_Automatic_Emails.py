import smtplib
import random
import os

def send_automatic_email():
    user = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    message = (f"Hi {user}, Welcome to myblog, Subscribe to our channel for more updates")

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("Your Gmail Account", "your Password")
    s.sendmail('&&&&&&',email,message)
    print("Email Sent!")
send_automatic_email()


