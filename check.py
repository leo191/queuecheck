import requests as rq
import json
import getpass
import xmltodict
import time


username = #input("username: ")
password = #getpass.getpass("Password")



def checkAndBreak(mailsub):
	while True:
		res = rq.get("https://mail.google.com/mail/feed/atom",auth=(username, password))
		emailjson=json.loads(json.dumps(xmltodict.parse(res.text)))
		emailsub = []

		for entry in emailjson['feed']['entry']:
			#emailsub.append(entry["title"])
			if mailsub == entry["title"]:
				exit(1)
		sleep(5)	

