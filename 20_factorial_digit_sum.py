import time


def factorial(n):
  if n == 0: return 1
  else: 
    return n*factorial(n-1)
  

def sum_of_digits(n):
  sum_ = 0
  n_str = str(n)
  for i in range(0, len(n_str)):
    sum_ = sum_ + int(n_str[i])
  return sum_

start = time.time()

N = 100
sum_ = sum_of_digits(factorial(N))

elapsed = time.time() - start
print(sum_)
print(elapsed)
