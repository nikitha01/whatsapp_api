from twilio.rest import Client
from two import quote1

account_sid = '****************************'
auth_token = '**********************'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = quote1,
    from_= 'whatsapp:+14155238886',
    to= 'whatsapp:+911234567890'
)

print(message.sid)