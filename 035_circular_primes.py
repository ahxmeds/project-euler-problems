#To reduce the runtime, I used two dictionaries, one to store the numbers already checked for primes, and another
#to store the circular prime numbers. The number containing the digit zero were immediately removed since they cannot
#be circular primes because upon circulating the zero to the end of the number, the number would always be divisible by 10;

#Answer = 55
#Time = 2.4995970726013184 s


import time
import math as m


def is_prime(number):
  if number <= 1: return False
  elif number == 2: return True
  elif number%2 == 0: return False
  else:
    for i in range(3, int(m.sqrt(number))+1, 2):
      if(number%i == 0):
        return False
  return True

def find_next_in_circle(number):
  str_num = str(number)
  length = len(str_num)
  next_num = ""
  for i in range(1, length):
  	next_num = next_num + str_num[i]
  
  next_num = next_num + str_num[0]
 
  return int(next_num)

def get_circular_numbers(number):
  length = len(str(number))
  array_circular_number = []
  array_circular_number.append(number)
  current_num = number
  for i in range(2, length+1):
    current_num = find_next_in_circle(current_num)
    array_circular_number.append(current_num)
  return array_circular_number

def contains_zero(number):
	str_num = str(number)
	flag = 0
	for i in range(0, len(str_num)):
		if str_num[i] == '0':
			flag = 1
			break
	if flag == 1:
		return True
	else: 
		return False



start = time.time()

dictionary_of_primes = {}
dictionary_of_circular_primes = {}
count = 0

for num in range(2, 1000001):
	if contains_zero(num) == False:
		if num in dictionary_of_primes:
			if num in dictionary_of_circular_primes:
				pass
			
			else:
				array_circular_number = get_circular_numbers(num)
				flag = 0
				for value in array_circular_number:
					if value not in dictionary_of_primes:
						if is_prime(value):
							dictionary_of_primes[value] = value
						else:
							flag = 1
							break
				
				if flag == 0:
					for value in array_circular_number:
						if value not in dictionary_of_circular_primes:
							dictionary_of_circular_primes[value] = value
						
						

		else:
			if is_prime(num):
				dictionary_of_primes[num] = num
				array_circular_number = get_circular_numbers(num)
				flag = 0
				for value in array_circular_number:
					if value not in dictionary_of_primes:
						if is_prime(value):
							dictionary_of_primes[value] = value
						else:
							flag = 1
							break
				
				if flag == 0:
					for value in array_circular_number:
						if value not in dictionary_of_circular_primes:
							dictionary_of_circular_primes[value] = value
						
						
elapsed = time.time() - start

print(len(dictionary_of_circular_primes))
print(dictionary_of_circular_primes)
print(elapsed)

