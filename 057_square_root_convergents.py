#Very ingenious problem. I ended up writing all the function for adding fraction, reducing fractions to lowest term, etc.
#but was getting MemoryError at n = 27th iteration. Later, realized that for the n-th iteration, the numerator and denominator
#are related to the (n-1)th iteration as follows:
#num(n) = num(n-1) + 2*den(n-1)
#den(n) = num(n-1) + den(n-1)
#Which made the problem pretty easy.


#Answer = 153
#Time = 0.08711504936218262 s


import time
import numpy as np
import math as m

def prime_factorization(number):
	prime_factors_list = []

	while number%2 == 0:
		prime_factors_list.append(int(2))
		number = number/2

	for i in range(3, int(m.sqrt(number))+1, 2):
		while number%i == 0:
			prime_factors_list.append(int(i))
			number = number/i

	if number > 2:
		prime_factors_list.append(int(number))

	return prime_factors_list


def lowest_term_fraction(num, den):

	prime_factor_num = np.array(prime_factorization(num))
	prime_factor_den = np.array(prime_factorization(den))

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


def invert_fraction(num, den):
	denominator = num
	numerator = den

	return numerator, denominator


def sum_of_fractions(a,b,c,d):
	numerator = a*d + b*c
	denominator = b*d
	lowest_num, lowest_den = lowest_term_fraction(numerator, denominator)
	return lowest_num, lowest_den


#When this function is used, the program runs out of memory at n = 27-th iteration 
#Hence, using the next function. None of the functions defined above will be used.
'''
def value_at_nth_iteration(n):
	if n == 1:
		return 3, 2
	else:
		_sum_n = 2
		_sum_d = 1
		for i in range(0, n-1):
			_sum_n, _sum_d = invert_fraction(_sum_n, _sum_d)
			_sum_n, _sum_d = sum_of_fractions(2, 1, _sum_n, _sum_d)
		_sum_n, _sum_d = invert_fraction(_sum_n, _sum_d)
		num, den = sum_of_fractions(1, 1, _sum_n, _sum_d)
		return num, den
'''

def value_at_nth_iteration(n):
	p, q = 1, 1

	for i in range(0, n):
		p_temp = p
		q_temp = q
		p = p_temp + 2*q_temp
		q = p_temp + q_temp
	return p,q
		

def number_of_digits(number):
	return len(str(number))


start = time.time()


count = 0
for n in range(1, 1001):
	numm, denn = value_at_nth_iteration(n)
	if number_of_digits(numm) > number_of_digits(denn):
		count += 1

elapsed = time.time() - start

print(count)
print(elapsed)



