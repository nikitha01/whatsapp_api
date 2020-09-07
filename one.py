from twilio.rest import Client
from two import quote1

account_sid = 'AC7dd14446811265466752b7b0a7ffbff6'
auth_token = '6981dfa672c79301b669ca12cecdb45f'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = quote1,
    from_= 'whatsapp:+14155238886',
    to= 'whatsapp:+918880307211'
)

print(message.sid)