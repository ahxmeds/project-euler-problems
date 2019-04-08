#Saving the sum of divisors for already calculated numbers in a dictionary

#Answer = 31626
#Time = 1.3728384971618652 s


import math as m
import time

def sum_of_divisors(num):
  sum_ = 0
  for i in range(1, (num//2)+1):
    if num%i == 0: 
      sum_ = sum_ + i
  return sum_


start = time.time()

dictionary = {}

total  = 0

for a in range(2, 10001):
  if a not in dictionary:
     b = sum_of_divisors(a)
     dictionary[a] = b
     if b not in dictionary:
       c = sum_of_divisors(b)
       dictionary[b] = c
       if c == a and a != b:
         total = total + a + b


elapsed = time.time() - start

print(total)
print(elapsed)
