from mailjet_rest import Client
from check import checkAndBreak
import os



# Get your environment Mailjet keys
API_KEY = '4716c6d88b4d3d8a9ae3507ba834bb42'
API_SECRET = '30214f5c5ade691ae57e1c93144d0b81'


frommail= 'no-reply@groupeseb.com'
fromname= 'Mailjet Pilot'
subject= 'Your email flight plan!'
text= 'Dear passenger, welcome to Mailjet! May the delivery force be with you!'
htlm= '<h1>Testing</h1>'


mailjet = Client(auth=(API_KEY, API_SECRET), version='v3')
data = {
  'FromEmail': 'no-reply@groupeseb.com',
  'FromName': 'Mailjet Pilot',
  'Subject': 'Your email flight plan!',
  'Text-part': 'Dear passenger, welcome to Mailjet! May the delivery force be with you!',
  'Html-part': '<h1>Testing</h1>,
  'Recipients': [
                {
                        "Email": "subhadip.banerjee@edifixio.com"
                }
        ]
}
result = mailjet.send.create(data=data)
if result.status_code == 200:
	checkAndBreak(subject)
