from datetime import date
from datetime import timedelta

#weeks = [week1, week2, week3, week4]
#week1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# DayFound = False
# a = 0

# date = datetime.date.today() #Gets todays date

# day=datetime.datetime.strftime(date, '%A') #Gets todays days

# currentmonth = datetime.datetime.strftime(date, '%m-%Y')# Converts from Date to String format

# first = "1-" + currentmonth #Adds the First

# currentmonth = datetime.datetime.strptime(first, '%d-%m-%Y') #Convert from string to date format

# newDate = datetime.datetime.strftime(currentmonth, '%A') # Finds the Day on the first of the month

# #Finds Day Position
# while DayFound == False:
	
# 	if newDate == days[a]:
# 		DayFound == True
# 	else:
# 		a = a+1

year = 2012
month = 2

start_date = date(year, month, 1)

#go back to nearest monday
if start_date.weekday() != 0:

	start_date = start_date + timedelta(days=-start_date.weekday())

end_date = start_date + timedelta(days=34)

print start_date, end_date

#Sends Queries to the datastore and gets the results
#queries = mycalendar.models.Event.query(currentmonth >= datetime.date.today()).order(mycalendar.models.Event.date)

#print queries



#print weeks