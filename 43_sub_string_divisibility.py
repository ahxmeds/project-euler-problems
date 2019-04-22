#Probably not the most efficient solution. 
#Generating all permutations of numbers 0...9 in lexicographic order and checking for the condition.

#Answer = 16695334890
#Time = 21.08375120162964 s

import time

def factorial(n):
  if n == 0: return 1
  else: 
    return n*factorial(n-1)

def lexicographic_permutation_for_n_digits(array):
	permutation_list = []

	permutation_list.append(''.join(str(i) for i in array))

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
		permutation_list.append(''.join(str(i) for i in array))

	return permutation_list


def sub_string_divisibility(number):
	str_num = str(number)
	length = len(str_num)

	d2d3d4 = int(str_num[1] + str_num[2] + str_num[3])
	d3d4d5 = int(str_num[2] + str_num[3] + str_num[4])
	d4d5d6 = int(str_num[3] + str_num[4] + str_num[5])
	d5d6d7 = int(str_num[4] + str_num[5] + str_num[6])
	d6d7d8 = int(str_num[5] + str_num[6] + str_num[7])
	d7d8d9 = int(str_num[6] + str_num[7] + str_num[8])
	d8d9d10 = int(str_num[7] + str_num[8] + str_num[9])

	if d2d3d4%2 == 0 and d3d4d5%3 == 0 and d4d5d6%5 == 0 and d5d6d7%7 == 0 and d6d7d8%11 == 0 and d7d8d9%13 == 0 and d8d9d10%17 == 0:
		return True
	else:
		return False


start = time.time()

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

all_permutations = lexicographic_permutation_for_n_digits(array)
answer_array = []

for num in all_permutations:
	if sub_string_divisibility(num):
		answer_array.append(int(num))

_sum = sum(answer_array)
elapsed = time.time() - start

print(_sum)
print(answer_array)
print(elapsed)

