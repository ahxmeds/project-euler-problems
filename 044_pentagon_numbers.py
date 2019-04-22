#Not a complete solution as I am not really checking for the lowest D. 
#Apparently the first pair for which the sum and difference are pentagonal also has the lowest D.

#Answer = 5482660
#Time = 1.7589201927185059 s


import time
import math as m


def is_pentagon_number(number):
	#solving the quadratic equation 3n^2 - n -2(number) = 0

	n = (1 + m.sqrt(1 + 24*number))/6

	if m.floor(n) == n:
		if (n*(3*n-1))/2 == number:
			return True
	else:
		return False


def nth_pentagon_number(n):
	return (n*(3*n-1))/2

start = time.time()

D_min = 0
found = 0
j = 1

while not found:
	for k in range(1, j):
		kth = nth_pentagon_number(k)
		jth = nth_pentagon_number(j)

		if is_pentagon_number(kth+jth) and is_pentagon_number(abs(jth - kth)):
			D_min = abs(jth - kth)
			k_min = k
			j_min = j
			found = 1
			break

	j += 1

elapsed = time.time() - start

print(D_min)
print(k_min, j_min)
print(elapsed)

