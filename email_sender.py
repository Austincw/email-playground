import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "John Doe"
email["to"] = "<you_email@domain.com>"
email["subject"] = "<text_here>"

# email.set_content(html.substitute({"name": "jojo"}), "html")
email.set_content("<content_here>")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email", "pwd")
    smtp.send_message(email)
    print("all done")
