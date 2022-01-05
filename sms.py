import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Your Account SID from twilio.com/console
#account_sid  = os.getenv("TWILIO_SID")
# Your Auth Token from twilio.com/console
#auth_token  = os.getenv("TWILIO_TOKEN")

#client = Client(account_sid, auth_token)

#message = client.messages.create(
#    to="+13092581204",
#    from_= os.getenv("TWILIO_NUMBER"),
#    body="test")

#print(message.sid)

def send_sms(dest_number,content):

    account_sid  = os.getenv("TWILIO_SID")
    auth_token  = os.getenv("TWILIO_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=dest_number,
        from_= os.getenv("TWILIO_NUMBER"),
        body=str(content))
    return

if __name__ == "__main__":
    pass
