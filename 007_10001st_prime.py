#Answer = 104743
#Time = 0.1518256664276123 s

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
    




def find_nth_prime(n):
  count = 0
  i = 2

  while count < n:
    if is_prime(i) == True:
      count = count + 1
      nth_prime = i
      print(count, " : ", i)
                
    i = i + 1 
     
  return nth_prime

start = time.time()
x = find_nth_prime(10001)

elapsed = time.time() - start
print(x)
print(elapsed)
