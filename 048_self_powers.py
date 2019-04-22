#Easy to solve in python due to the BigInteger support.

#Answer = 9110846700
#Time = 0.00797581672668457 s


import time

start = time.time()

_sum = 0
for i in range(1, 1001):
	_sum += i**i

last_10_digits = _sum%(10**10)
elapsed = time.time() - start

print(last_10_digits)
print(elapsed)