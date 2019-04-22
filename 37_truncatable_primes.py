#Maintaining a dictionary for all numbers denoting prime or not

#Answer = 748317
#Time = 1.7377028465270996 s


import time
import math as m

boolean_dictionary_of_primes = {}


def is_prime(number):
  if number <= 1: return False
  elif number == 2: return True
  elif number%2 == 0: return False
  else:
    for i in range(3, int(m.sqrt(number))+1, 2):
      if(number%i == 0):
        return False
  return True


def left_to_right_truncation(number):
	str_num = str(number)
	length = len(str_num)
	l2r_truncated_numbers = []
	l2r_truncated_numbers.append(number)

	for i in range(1, length):
		current = ""
		for j in range(i, length):
			current = current + str_num[j]
		l2r_truncated_numbers.append(int(current))
	return l2r_truncated_numbers


def right_to_left_truncation(number):
	str_num = str(number)
	length = len(str_num)
	r2l_truncated_numbers = []
	r2l_truncated_numbers.append(number)

	for i in range(0, length-1):
		current = ""
		for j in range(0, length - i - 1):
			current = current + str_num[j]
		r2l_truncated_numbers.append(int(current))
	return r2l_truncated_numbers


def check_list_for_all_primes(_list_):
	global boolean_dictionary_of_primes
	flag = 0
	for value in _list_:
		if value not in boolean_dictionary_of_primes:
			if is_prime(value) == True:
				boolean_dictionary_of_primes[value] = True
			else:
				boolean_dictionary_of_primes[value] = False
				flag = 1
				break
		else: 
			if boolean_dictionary_of_primes[value] == False:
				flag = 1
				break
			else:
				pass

	if flag == 0: 
		return True
	else:
		return False


start = time.time()

num = 11
count = 0
_sum = 0
answer_numbers = []

while count < 11:
	if is_prime(num) == True:
		boolean_dictionary_of_primes[num] = True
		l2r_truncated_numbers = left_to_right_truncation(num)
		r2l_truncated_numbers = right_to_left_truncation(num)

		bool_l2r = check_list_for_all_primes(l2r_truncated_numbers)
		bool_r2l = check_list_for_all_primes(r2l_truncated_numbers)

		if bool_l2r == True and bool_r2l == True:
			answer_numbers.append(num)
			_sum += num
			count += 1
			num += 2
		else:
			num += 2
	else:
		boolean_dictionary_of_primes[num] = False
		num += 2

elapsed = time.time() - start

print(_sum)
print(answer_numbers)
print(elapsed)