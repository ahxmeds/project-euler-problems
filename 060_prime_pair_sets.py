#Generating a list of primes till 10000.

#Answer = 26033
#Time = 9.885305643081665 s


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


def concat(a,b):
	len_a = m.floor(m.log10(a))+1
	len_b = m.floor(m.log10(b))+1
	if is_prime(int(a*(10**len_b)+b)) and is_prime(int(b*(10**len_a)+a)):
		return True
	return False


def build_prime_list_till_N(N):
  prime_list = [3]
  for i in range(7,N):
    if is_prime(i) == True:
    	prime_list.append(i)
  return prime_list


def find_5_primes():
	prime_list = build_prime_list_till_N(10000)

	for a in prime_list:
		for b in prime_list:
			if b < a:
				continue
			if concat(a, b):
				for c in prime_list:
					if c < b:
						continue
					if concat(a,c) and concat(b,c):
						for d in prime_list:
							if d < c:
								continue
							if concat(a, d) and concat(b,d) and concat(c,d):
								for e in prime_list:
									if e < d:
										continue
									if concat(a, e) and concat(b,e) and concat(c,e) and concat(d,e):
										return a, b, c, d, e, (a+b+c+d+e)

start = time.time()

a, b, c, d, e, _sum =  find_5_primes()

elapsed = time.time() - start

print(a, b, c, d, e)
print(_sum)
print(elapsed)

