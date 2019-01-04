from datetime import datetime,timedelta
d = datetime.now()

d1 = d+timedelta(minutes=20)

if d < d1:
  print('Hello'+ str(d1))
