#The idea was to figure out the limits till which one must check
#for both the value of number and the corresponding value of n in (1,2,...,n).

#Answer = 932718654
#Time = 0.026198625564575195 s

import time

def is_pandigital(number):
  str_num = str(number)
  length = len(str_num)
  if length == 9:
    set_digits_ref = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    digits = []
    for i in range(0, len(str_num)):
      digits.append(int(str_num[i]))
    set_digits = set(digits)
    set_intersection = set_digits_ref & set_digits

    if set_intersection == set_digits_ref:
      return True
    else:
      return False
  else:
    return False

def get_concat_number(num, array):
	string = ""
	for value in array:
		product = num*value
		string += str(product)

	number = int(string)
	return number


start = time.time()

vector_1_dig = [1, 2, 3, 4, 5]
vector_2_dig = [1, 2, 3, 4]
vector_3_dig = [1, 2]
vector_4_dig = [1, 2]

vector_dig_dictionary = {1:vector_1_dig, 2:vector_2_dig, 3:vector_3_dig, 4:vector_4_dig}
largest_pandigital = 0

for num in range(1, 10000):
	length = len(str(num))
	concat = get_concat_number(num, vector_dig_dictionary[length])
	if is_pandigital(concat):
		if concat > largest_pandigital:
			largest_pandigital = concat

elapsed = time.time() - start

print(largest_pandigital)
print(elapsed)