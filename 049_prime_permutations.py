import time

def is_prime(number):
  if number <= 1: return False
  elif number == 2: return True
  elif number%2 == 0: return False
  else:
    for i in range(3, int(m.sqrt(number))+1, 2):
      if(number%i == 0):
        return False
  return True

def lexicographic_permutation_for_n_digits(array):
	permutation_list = []

	permutation_list.append(int(''.join(str(i) for i in array)))

	total_permutations = factorial(len(array))
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

def convert_num_to_array(num):
	array = []
	str_num = str(num)

	for i in range(0, len(str_num)):
		array.append(int(str_num[i]))
	return array

dictionary_of_primes = {}

for num in range(1001, 9999, 2):
	if num in dictionary_of_primes:
		if dictionary_of_primes[num] == True:
			permutation_list = lexicographic_permutation_for_n_digits(convert_num_to_array(num))

			for value in permutation_list:
				if value in dictionary_of_primes:
					if dictionary_of_primes[value] == True:
			
		else:
			pass
	else:
		if is_prime(num):
			dictionary_of_primes[num] = True
		else:
			dictionary_of_primes[num] = False