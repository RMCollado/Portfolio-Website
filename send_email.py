import smtplib
import os


def send_email(message):
    username = "richcolladopydev@gmail.com"
    password = os.getenv("PYDEVEMAILPASSWORD")

    receiver = "richcolladopydev@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls() and server.login(user=username, password=password)
        server.sendmail(
            from_addr=username,
            to_addrs=receiver,
            msg=message
        )
