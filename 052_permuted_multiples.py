#Answer = 142857
#Time = 0.33245086669921875 s

import time

def get_unique_digits(number):
	str_num = str(number)
	length = len(str_num)
	digits = []

	for i in range(0, length):
		digits.append(str_num[i])
	set_digits = set(digits)

	return set_digits


start = time.time()

x = 1

while True:
	if get_unique_digits(2*x) == get_unique_digits(3*x) == get_unique_digits(4*x) == get_unique_digits(5*x) == get_unique_digits(6*x):
		smallest_num = x
		break

	else:
		x += 1

elapsed = time.time() - start
print("x =",smallest_num)
print("2x = ", smallest_num*2,"\n3x = ",smallest_num*3, "\n4x = ", smallest_num*4, "\n5x = ", smallest_num*5, "\n6x = ", smallest_num*6)
print(elapsed)