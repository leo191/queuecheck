import requests as rq
import json
import getpass
import xmltodict
import datetime
import sys

username = 'humblebeastleo' #input("username: ")
password = 'Life7679' #getpass.getpass("Password")

log_fail = open('/var/log/mailcheck','w') 


def checkAndBreak(mailsub):
	print(sys.version)
	mailsub = "Critical security alert"
	while True:
		ETW = 3
		while ETW > 0:
			res = rq.get("https://mail.google.com/mail/feed/atom",auth=(username, password))
			print(res.text)
			emailjson=json.loads(json.dumps(xmltodict.parse(res.text)))
			emailsub = []
			for entry in emailjson['feed']['entry']:
				#emailsub.append(entry["title"])				
				if mailsub == entry["title"]:
					#log_fail.write("Mail found with ---" + mailsub + "--- subject :" + str(datetime.datetime.now()) +"\n")
					log_fail.write('0')
					exit(0)
			ETW -= 1
		#log_fail.write("No mails from ---"+ mailsub + "--- subject :" + str(datetime.datetime.now()) +"\n")
		log_fail.write('1')

         

checkAndBreak("")
