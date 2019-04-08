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
    

sum_ = 0

for i in range(2, 2000001):
  if is_prime(i):
    sum_ = sum_ + i

print(sum_)
