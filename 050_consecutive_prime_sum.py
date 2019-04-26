import time
import math as m

def is_prime(number):
  if number <= 1: return False
  elif number == 2: return True
  elif number%2 == 0: return False
  else:
    for i in range(3, int(m.sqrt(number))+1, 2):
      if(number%i == 0):
        return False
  return True

def build_prime_list_below_N(N):
	prime_dictt = {}
	for num in range(1,N):
		if is_prime(num):
			prime_dictt[num] = num

	return prime_dictt

def get_sum(array, start, length)

dictt_of_primes_below_1m = build_prime_list_below_N(1000000)



for i in range()

