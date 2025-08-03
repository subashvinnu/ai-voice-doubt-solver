from twilio.rest import Client


account_sid = 'AC56a2c06cd537e467e6630ae04be5dfa0'
auth_token = '4c65a56b70ef58a927c0ee5e3985029'
client = Client(account_sid, auth_token)

call = client.calls.create(
    to='+919701793589',  
    from_='+918179631961',  
    url='http://demo.twilio.com/docs/voice.xml'
)

print("Call initiated")
