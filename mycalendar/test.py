from datetime import date
import datetime

currentdate = date.today()
otherdate = date.today()
anotherdate = date.today()
anotherdate = int(date.strftime(anotherdate , '%d'))
otherdate = int(date.strftime(otherdate, '%m'))
currentdate = int(date.strftime(currentdate, '%d%m%y'))
otherdate += 1
if otherdate == 13:
	nextdate = "1"
else:
	currentdate += 100
	if anotherdate < 10:
		nextdate = '0' + str(currentdate)
	else:
		nextdate = str(currentdate)
nextdate = datetime.datetime.strptime(nextdate , '%d%m%y')