# Fetch Emails
# pip install imap-tools
from imap_tools import MailBox
def Fetch_Email(user, pwd):
    mbox = MailBox('imap.gmail.com').login(user, pwd, "INBOX")
    for email in mbox.fetch():
        print(email.date, email.subject, len(email.text or email.html))
        
Fetch_Email("crupib@gmail.com", "Paul6464!")
