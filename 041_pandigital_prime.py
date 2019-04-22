#Used the lexicographic permutation for generating for the all the n-digit pandigital numbers for each number n = 1...9.

#Answer = 7652413
#Time =  1.7579646110534668 s

import time
import math as m

def build_dictionary_digits_ref():
	dictionary = {} 
	for i in range(1, 10):
		array = []
		for j in range(1, i+1):
			array.append(j)
		dictionary[i] = array
	return dictionary


def factorial(n):
	if n == 0: return 1
	else: return n*factorial(n-1)


def lexicographic_permutation_for_n_digits(array):
	permutation_list = []

	permutation_list.append(int(''.join(str(i) for i in array)))

	total_permutations = factorial(len(array)) #can use this in the for loop below for calculating all the permutations 
	                                         #lexicographic order
	for count in range(2, total_permutations+1):
		max_k = 0	
		for k in range(0, len(array)-1):
			if array[k] < array[k+1]:
				if k > max_k:
					max_k = k

		max_l = max_k
		for l in range(max_k + 1, len(array)):
			if array[l] > array[max_k]:
				if l > max_l:
					max_l = l

		array[max_k], array[max_l] = array[max_l], array[max_k] #python swap
		array[max_k+1:len(array)] = reversed(array[max_k+1:len(array)])
		permutation_list.append(int(''.join(str(i) for i in array)))

	return permutation_list


def is_prime(number):
  if number <= 1: return False
  elif number == 2: return True
  elif number%2 == 0: return False
  else:
    for i in range(3, int(m.sqrt(number))+1, 2):
      if(number%i == 0):
        return False
  return True



start = time.time()

largest_pandigital_prime = 0
dictionary_of_digits_ref = build_dictionary_digits_ref()
dictionary_of_n_pandigital_numbers = {}

for item in dictionary_of_digits_ref:
	array = dictionary_of_digits_ref[item]
	dictionary_of_n_pandigital_numbers[item] = lexicographic_permutation_for_n_digits(array)

for item in dictionary_of_n_pandigital_numbers:
	for value in dictionary_of_n_pandigital_numbers[item]:
		if value%2 != 0:
			if is_prime(value):
				if value > largest_pandigital_prime:
					largest_pandigital_prime = value

elapsed = time.time() - start

print(largest_pandigital_prime)
print(elapsed)