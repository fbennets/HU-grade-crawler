from twilio.rest import Client
from creds import *


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = account
auth_token = auth
client = Client(account_sid, auth_token)

def sms_sender(number, type, grade):
    message = client.messages \
                    .create(
                         body="Du hast in der " + type + " " + grade + " Punkte. Glückwunsch!",
                         from_='+447723442078',
                         to=number
                     )

    print(message.sid)
