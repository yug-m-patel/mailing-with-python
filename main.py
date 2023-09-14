import smtplib
import ssl

sender ="yugpatel2713@gmail.com"
reciver ="at0121cse675@gmail.com"
password ="hkihudzjdnhabsvc"
subject = "Email by python"
body = "  "
cOntext = ssl.create_default_context()

message = f"""From: oii{sender}
To: oyeeee{reciver}
Subject: {subject}\n
{body}
"""


server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls(context=cOntext)

server.login(sender, password)
print("logged in")
server.sendmail(sender, reciver, message)
print("scuess")