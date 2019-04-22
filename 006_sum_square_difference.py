#Answer = 25164150
#Time = 2.9087066650390625e-05 s


import time 

start = time.time()

def sum_of_square(a, b):
  sum_of_square = 0
  for i in range(a, b+1):
    sum_of_square = sum_of_square + i*i
  return sum_of_square

def square_of_sum(a, b):
  sum_ = 0
  for i in range(a, b+1):
    sum_ = sum_ + i 
  square_of_sum = sum_*sum_
  return square_of_sum 


sum_sq = sum_of_square(1, 100)
sq_sum = square_of_sum(1, 100)

difference = sq_sum - sum_sq
elapsed = time.time() - start

print(difference)
print(elapsed)
