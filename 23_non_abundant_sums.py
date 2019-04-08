#Probably not the most efficient implementation because I precalculated all the abundant numbers before finding the numbers that can be expressed as their sums. 
#The code ran pretty fast nevertheless because of the fast indexing using dictionary.

#Answer = 4179871
#Time = 0.7072253227233887 s

import time
import math as m


#Sum of proper divisors
def sum_of_divisors(num):
  sum_ = 1
  for i in range(2, int(m.sqrt(num))+1):
    if num%i == 0:
      if i == num/i:
        sum_ += i
      else:  	
        sum_ += i + num/i
  return sum_

#returns whether the number is deficient, abundant or perfect
def type_of_number(num):
  sum_ = sum_of_divisors(num)
  if sum_ == num:
  	return 0 #perfect number
  elif sum_ > num:
  	return 1 #abundant number
  else:
  	return -1 #deficient number


start = time.time()  

LIMIT = 28123

abundant = []

for i in range(1,LIMIT+1):
	if type_of_number(i) == 1:
		abundant.append(i)

dictionary_abundant = {i : i for i in abundant}

_sum_ = 0

for num in range(1, LIMIT+1):
	found = 0
	for i in abundant:
		if i < num:
			if (num - i) in dictionary_abundant:
				found = 1
				break
		else: 
			break
	if found == 0: #if cannot express as the sum of two abundant numbers, then add it to the total
		_sum_ += num


elapsed = time.time() - start		

print(_sum_)
print(elapsed)