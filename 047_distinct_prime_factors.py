#Answer = 134043
#Time = 1.223299503326416 s


import time 
import math as m


def prime_factorization(number):
	prime_factors_list = []

	while number%2 == 0:
		prime_factors_list.append(2)
		number = number/2

	for i in range(3, int(m.sqrt(number))+1, 2):
		while number%i ==0:
			prime_factors_list.append(int(i))
			number = number/i

	if number > 2:
		prime_factors_list.append(number)

	return prime_factors_list


start = time.time()

start_num = 2
pf1 = prime_factorization(start_num)
pf2 = prime_factorization(start_num + 1)
pf3 = prime_factorization(start_num + 2)
pf4 = prime_factorization(start_num + 3)

while True:
	if len(set(pf1)) == 4 and len(set(pf2)) == 4 and len(set(pf3)) == 4 and len(set(pf4)) == 4:
		first_num = start_num
		break
	else:
		pf1 = pf2
		pf2 = pf3
		pf3 = pf4
		start_num += 1	
		pf4 = prime_factorization(start_num + 3)
		
elapsed = time.time() - start

print(first_num, first_num+1, first_num+2, first_num+3)
print(elapsed)
