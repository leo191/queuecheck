import requests as rq
import json
import getpass
import xmltodict


username = "subhadipbanerjee527"	#input("username: ")
password = "Subhadip7679680429"		#getpass.getpass("Password")



def checkAndBreak(mailsub):
	res = rq.get("https://mail.google.com/mail/feed/atom",auth=(username, password))


	emailjson=json.loads(json.dumps(xmltodict.parse(res.text)))
	emailsub = []

	for entry in emailjson['feed']['entry']:
		#emailsub.append(entry["title"])
		if mailsub == entry["title"]:
			exit(1)


