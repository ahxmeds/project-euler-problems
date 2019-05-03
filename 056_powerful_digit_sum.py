#Answer = 972
#Time = 0.239377975464 s

import time

def digital_sum(number):
	str_num = str(number)
	_sum = 0

	for i in range(0, len(str_num)):
		_sum += int(str_num[i])

	return _sum

start = time.time()
max_value = 0

for a in range(1, 100):
	for b in range(1, 100):
		if digital_sum(a**b) > max_value:
			max_value = digital_sum(a**b)

elapsed = time.time() - start

print(max_value) 
print(elapsed)