from twilio.rest import TwilioRestClient

accountSID = 'ACxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxx'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+14955551234'
myCellPhone = '+14955558888'
message = twilioCli.messages.create(body = 'Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)

print(message.to)
print(message.from_)
print(message.body)
print(message.status)
print(message.date_created)
print(message.date_sent == None)
print(message.sid)
updatedMessage = twilioCli.messages.get(message.sid)
print(updatedMessage.status)
print(updatedMessage.date_sent)
