#Answer = 5777
#Time = 0.5067565441131592 s

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
    

def get_all_primes_smaller_than_number(number):
	global dictionary_of_primes
	prime_list = [2, 3, 5, 7]
	for num in range(9, number+1, 2):
		if num in dictionary_of_primes:
			if dictionary_of_primes[num] == True:
				prime_list.append(num)
			elif dictionary_of_primes[num] == False:
				pass
		else:
			if is_prime(num):
				dictionary_of_primes[num] = True
				prime_list.append()
			else:
				dictionary_of_primes[num] = False
	return prime_list


start = time.time()

dictionary_of_primes = {}
num = 9
smallest_num = 0

while True:
	flag = 0
	if is_prime(num) == False:
		if num not in dictionary_of_primes:
			dictionary_of_primes[num] = False
		prime_list = get_all_primes_smaller_than_number(num)

		for value in prime_list:
			sq_num = m.sqrt((num - value)/2)
			if m.floor(sq_num) == sq_num:
				flag = 1
				break

		if flag == 0:
			smallest_num = num
			break
		else:
			num += 2


	else:
		if num not in dictionary_of_primes:
			dictionary_of_primes[num] = True
		num += 2

elapsed = time.time() - start

print(smallest_num)
print(elapsed)