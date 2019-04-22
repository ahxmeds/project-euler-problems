#Answer = -59231
#Time = 7.809332609176636 s

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
    

def polynomial_at_n(n, a, b):
	return (n**2 + a*n + b)


start = time.time()
dictionary_of_primes = {}

for a in range(-999, 1000):
  for b in range(-1000, 1001):
    n = 0
    dictionary_of_primes[(a,b)] = [a, b] #storing the a, b values as the first two elements of the list
    while True:
      if is_prime(polynomial_at_n(n, a, b)):
        dictionary_of_primes[(a,b)].append([n])  
        n += 1     
      else:
      	break

max_length = 0

for key in dictionary_of_primes:
  if len(dictionary_of_primes[key])-2 > max_length:
    max_length = len(dictionary_of_primes[key])
    product = dictionary_of_primes[key][0]*dictionary_of_primes[key][1]
    
elapsed = time.time() - start

print(product)
print(elapsed)
