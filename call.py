import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

#account_sid  = os.getenv("TWILIO_SID")
#auth_token  = os.getenv("TWILIO_TOKEN")

#client = Client(account_sid, auth_token)

#message = client.messages.create(
#    to="+<HARDCODE>",
#    from_= os.getenv("TWILIO_NUMBER"),
#    body="test")

#print(message.sid)

def make_call(dest_number,content):

    account_sid  = os.getenv("TWILIO_SID")
    auth_token  = os.getenv("TWILIO_TOKEN")
    client = Client(account_sid, auth_token)
    voice=f"<Response><Say>The shop temperature is {content} degrees.</Say></Response>",


    call = client.calls.create(
        #url='http://handler.twilio.com/twiml/<CLIENTURL>',
        twiml=voice,
        to=dest_number,
        from_= os.getenv("TWILIO_NUMBER"))
    return

if __name__ == "__main__":
    pass
