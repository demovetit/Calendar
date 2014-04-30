import datetime
import mycalendar
import mycalendar.models
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

DayFound = False
a = 0

date = datetime.date.today() #Gets todays date

day=datetime.datetime.strftime(date, '%A') #Gets todays days

currentmonth = datetime.datetime.strftime(date, '%m-%Y')# Converts from Date to String format

first = "1-" + currentmonth #Adds the First

currentmonth = datetime.datetime.strptime(first, '%d-%m-%Y') #Convert from string to date format

newDate = datetime.datetime.strftime(currentmonth, '%A') # Finds the Day on the first of the month

#Finds Day Position
while DayFound == False:
	
	if newDate == days[a]:
		DayFound == True
	else:
		a = a+1

#Sends Queries to the datastore and gets the results
queries = mycalendar.models.Event.query(currentmonth >= datetime.date.today()).order(mycalendar.models.Event.date)

print queries


#for i in range(5):#Rows Loop
	

	#for j in range(a, 7): #Columns Loop

