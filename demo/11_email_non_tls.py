#!/usr/local/bin/python3
import section, smtplib, json, email.message

json_file = open("config.json")
gmail_cfg = json.load(json_file)
msg = email.message.EmailMessage()
msg["to"] = gmail_cfg["toemail"]
msg["from"] = gmail_cfg["email"]
msg["Subject"] = "Send email with Python"
msg.set_content("Hi! this email was sent from Python script !")
with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp:
    smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
    smtp.send_message(msg)
