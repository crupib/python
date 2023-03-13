#!/usr/local/bin/python3
import smtplib

# creates SMTP session
# s = smtplib.SMTP('142.251.163.109', 587)
s = smtplib.SMTP("smtp.gmail.com", 587)

# start TLS for security
s.starttls()

# Authentication
s.login("crupib@gmail.com", "zjyezlpeopobsgzc")

# message to be sent
message = """From: From God <from@fromdomain.com>
To: Peasant <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
# sending the mail
s.sendmail("crupib@gmail.com", "crupib@hotmail.com", message)

# terminating the session
s.quit()
