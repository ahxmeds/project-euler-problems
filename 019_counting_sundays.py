#Used the Sakamoto's algorithm given in the Wikipedia article https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Sakamoto's_methods.
#This method creates a virtual year such that the year starts on March 1 and ends on 28 or 29 February (depending on whether leap or not)
#With just dd/mm/yyyy as input, the algorithm gives 0 for Sun, 1 for Mon,..., 6 for Sat.

#The problem became easy as I didn't have to check for leap year
#(though a function is included for doing so, but never used) or iterate over all days.

#Answer = 171
#Time = 0.0012617111206054688 s

import time


def day_of_week(dd, mm, yyyy):
	t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	yyyy = yyyy - (mm<3)  #subtract 1 for mm = Jan and Feb, otherwise subtract 0

	return (yyyy + int(yyyy/4) - int(yyyy/100) + int(yyyy/400) + t[mm-1] + dd) % 7


def is_leap_year(yyyy):
	if yyyy%100 == 0:
		if yyyy%400 == 0:
			return True
		else:
			return False

	if yyyy%4 == 0:
		return True
	else:
		return False

start = time.time()
count = 0

for year in range(1901, 2001):
	for month in range(1, 13):
		if day_of_week(1, month, year) == 0:
			count += 1

elapsed = time.time() - start

print(count)
print(elapsed)

