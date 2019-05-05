#The idea was to find the upper and lower bounds on x^n given x^n is an n-digit number. 
#Using this fact, the bounds were 10^(n-1) <= x^n < 10^n => 10^((n-1)/n) <= x <= 9.
#In the limit of n->\infty, the expression (n-1)/n -> 1, so the lower bound -> 10, which is greater than the upper bound of 9 
#The inequality was tested for each n starting with n = 1, until the lower bound surpassed the upper bound.

#Answer = 49
#Time = 3.528594970703125e-05 s

import time
import math as m 


start = time.time()

upper_bound = 10
n = 1
lower_bound = m.ceil(pow(10, (n-1)/n))

count = 0

while (lower_bound < upper_bound):
	count += upper_bound - lower_bound 
	n = n + 1
	lower_bound = m.ceil(pow(10, (n-1)/n))


elapsed = time.time() - start

print(count)
print(elapsed)