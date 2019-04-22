#Pretty easy problem.

#Answer = 1533776805  
#Time = 0.03949165344238281 s

import time
import math as m

def nth_triangle_number(n):
	return (n*(n+1))/2

def is_pentagonal_number(number):
	#solving the quadratic equation 3n^2 - n -2(number) = 0

	n = (1 + m.sqrt(1 + 24*number))/6

	if m.floor(n) == n:
		if (n*(3*n-1))/2 == number:
			return True
	else:
		return False

def is_hexogonal_number(number):
	#solving the quadratic equation 2n^2 - n - (number) = 0

	if (1 + m.sqrt(1 + 8*number))%4 == 0:
		return True
	else:
		return False

start = time.time()

n = 286
count = 0

while count < 1:
	tri_num = nth_triangle_number(n)
	if is_pentagonal_number(tri_num) == True and is_hexogonal_number(tri_num) == True:
		count += 1
		nth = n
	n += 1

elapsed = time.time() - start

print(tri_num)
print(nth)
print(elapsed)


