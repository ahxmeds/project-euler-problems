#One of my favourite problems. Simple yet elegant.

#Answer = 983
#Time = 0.06152844429016113 s

import time


def find_position_in_array(array, num):
	for i in range(0, len(array)):
		if array[i] == num:
			return i

def length_of_recurring_cycle(string):

	min_pos, max_pos = 0, 0

	for i in range(0, len(string)):
		if string[i] == '(':
			min_pos = i
		elif string[i] == ')':
			max_pos = i
	
	if max_pos == min_pos == 0:
		return 0
	else:
		return max_pos - min_pos - 1


def find_decimal_reciprocal(number):
	if number == 1:
		return '1'

	dict_remainders = {}
	remainder_list = []

	answer = '0.'
	remainder = 1%number 
	remainder_list.append(remainder)
	dict_remainders[remainder] = remainder
	dividend = 10*remainder

	quotient = []

	while remainder != 0:
		quotient.append(int(dividend/number))
		remainder = dividend%number
		if remainder in dict_remainders:
			rep_pos = find_position_in_array(remainder_list,remainder)
			break
		else:
			dict_remainders[remainder] = remainder
			remainder_list.append(remainder)
		dividend = 10*remainder 

	if remainder!= 0:
		for i in range(0, rep_pos):
			answer = answer + str(quotient[i])
		answer = answer + "("
		for i in range(rep_pos, len(quotient)):
			answer = answer + str(quotient[i])
		answer = answer + ")"
	return answer


start = time.time()

max_length = 0
for d in range(1, 1000):
	length = length_of_recurring_cycle(find_decimal_reciprocal(d))
	if length >= max_length:
		max_length = length
		max_d = d


elapsed = time.time() - start

print(max_d)
print(elapsed)