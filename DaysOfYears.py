# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def leap_year(year):
	if (year % 400) == 0:
		return True
	elif (year % 4) == 0 and (year % 100) != 0:
		return True
	return False

def nextDayMonth(year, month):
	if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
		return 31
	if(month == 4 or month == 6 or month == 9 or month == 11):
		return 30
		
	if(month == 2 and leap_year(year)):
		return 29
	else:
		return 28

def nextDay(year, month, day):
	if day < nextDayMonth(year, month):
		return year, month, day + 1
	else:
		if month == 12:
			return year + 1, 1, 1
		else:
			return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    year, month, day = year1, month1, day1
    days = 0
    while(dateIsBefore(year, month, day, year2, month2, day2)):
		year, month, day = nextDay(year, month, day)
		days += 1
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"
test()