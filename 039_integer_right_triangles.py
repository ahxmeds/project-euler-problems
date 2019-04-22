#For the sides of triangle a, b, c, we have a triple (a, b, c) with 0<a<=b<=c.
#The idea was to find the bounds on a, given it is the smallest number in the triple.
#Using that, the bounds on b can be fixed and the value of c can be calculated (c = p -a -b).
#Finally, for a given p, a solution (a, b, c) was tested for being right-triangle.

#Answer = 840
#Time = 5.166690826416016 s

import time
import math as m

def is_right_triangle(a, b, c):
	if a**2 + b**2 == c**2:
		return True
	else:
		return False

def find_total_right_triangles(perimeter):
	count = 0
	a_max = m.floor(perimeter/3)
	for a in range(1, a_max+1):
		b = m.floor(((perimeter - 2*a)/2)+1)
	
		if b < a:
			b = a
		c = perimeter - a - b

		while (c >= b):
			if is_right_triangle(a, b, c):
				count += 1
			b += 1
			c -= 1

	return count

start = time.time()

max_count = 0
for perimeter in range(1, 1001):
	count = find_total_right_triangles(perimeter)
	if count > max_count:
		max_count = count
		p = perimeter

elapsed = time.time() - start

print(p)
print(elapsed)