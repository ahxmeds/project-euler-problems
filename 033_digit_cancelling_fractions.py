#Extremely beautiful problem. Required a lot of work to make the code robust.
#Prime factorization algorithm has been used along with functions from numpy library
#to reduce the product to lowest form.

#Answer = 100
#Time = 0.012164592742919922


import time
import math as m
import numpy as np 

def common_present(num, den):
	str_num = str(num)
	str_den = str(den)
	common_num = list(set(str_num) & set(str_den))

	if len(common_num) == 0:
		return False
	else:
		if common_num[0] == '0':
			return False
		else:
			return True


def delete_common(string_number, string_comm):
	new_number = ""
	if string_number[0] == string_number[1]:
		return string_number[0]

	else:
		for i in range(0, len(string_number)):
			if string_number[i] != string_comm:
				new_number = string_number[i]
	return new_number


def cancel_common_numbers(num, den):
	str_num = str(num)
	str_den = str(den)
	common_num = list(set(str_num) & set(str_den))[0]
	new_num = int(delete_common(str_num, common_num))
	new_den = int(delete_common(str_den, common_num))

	return new_num, new_den


def prime_factorization(number):
	prime_factors_list = []

	while number%2 == 0:
		prime_factors_list.append(2)
		number = number/2

	for i in range(3, int(m.sqrt(number))+1, 2):
		while number%i ==0:
			prime_factors_list.append(i)
			number = number/i

	if number > 2:
		prime_factors_list.append(number)

	return prime_factors_list


def lowest_term_product_fraction(num_array, den_array):
	prod_num = 1
	prod_den = 1

	for i in range(0, len(num_array)):
		prod_num = prod_num*num_array[i]
		prod_den = prod_den*den_array[i]

	prime_factor_num = np.array(prime_factorization(prod_num))
	prime_factor_den = np.array(prime_factorization(prod_den))

	num_prime_counts = np.bincount(prime_factor_num)
	den_prime_counts = np.bincount(prime_factor_den)

	num_position = np.nonzero(num_prime_counts)[0]
	den_position = np.nonzero(den_prime_counts)[0]

	num_prime_factorization = np.vstack((num_position, num_prime_counts[num_position])).T
	den_prime_factorization = np.vstack((den_position, den_prime_counts[den_position])).T


	for i in num_prime_factorization:
		for j in den_prime_factorization:
			if i[0] == j[0]:
				if i[1] > j[1]:
					diff = i[1] - j[1]
					i[1] = diff
					j[1] = 0
				elif i[1] < j[1]:
					diff = j[1] - i[1]
					j[1] = diff
					i[1] = 0
				else:
					i[1] = 0
					j[1] = 0

	lowest_num = 1
	lowest_den = 1
	for i in num_prime_factorization:
		for j in range(0, i[1]):
			lowest_num = lowest_num*i[0]
	for i in den_prime_factorization:
		for j in range(0, i[1]):
			lowest_den = lowest_den*i[0]

	return lowest_num, lowest_den



start = time.time()

num_array = []
den_array = []

for numerator in range(10, 99):
	for denominator in range(numerator+1, 100):
		if common_present(numerator, denominator):
			new_num, new_den = cancel_common_numbers(numerator, denominator)
			if new_den == 0:
				pass
			elif new_num/new_den == numerator/denominator:
				num_array.append(numerator)
				den_array.append(denominator)

lowest_num, lowest_den = lowest_term_product_fraction(num_array, den_array)
elapsed = time.time() - start

print("Numerator = ", num_array)
print("Denominator = ", den_array)

print("Numerator = ", lowest_num)
print("Denominator = ", lowest_den)
print(elapsed)