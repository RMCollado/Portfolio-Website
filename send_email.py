import smtplib, ssl

host = "smtp.gmail.com"
port = 456

username = "richcolladopydev@gmail.com"
password = "zrjvrsgkkvegkioy"

receiver = "richcolladopydev@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
Hi!
How are you?
Bye
"""
with smtplib.SMTP("smtp.gmail.com") as server:
    server.starttls() and server.login(user=username, password=password)
    server.sendmail(
        from_addr=username,
        to_addrs=receiver,
        msg=message
    )