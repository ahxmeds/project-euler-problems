#Maintaining distinct elements in a dictionary

#Answer = 9183
#Time = 0.007146358489990234 s

import time

start = time.time()

dictionary_of_distinct_numbers = {}

for a in range(2, 101):
	for b in range(2, 101):
		num = pow(a, b)
		if num not in dictionary_of_distinct_numbers:
			dictionary_of_distinct_numbers[num] = num


elapsed = time.time() - start

print(len(dictionary_of_distinct_numbers))
print(elapsed)
