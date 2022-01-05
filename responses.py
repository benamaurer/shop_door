from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from temp import *

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms():

    number = request.form['From']
    message_body = request.form['Body']

    print(message_body)

    response_text = "Commands: temp"

    temp = ['temp','Temp','temperature','Temperature']
    if message_body in temp:
        response_text = f"The shop temperature is {read_temp()[1]} degrees."


    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
