#trivial solution in python 
#Answer = 1366
#Time = 0.00011038780212402344 s

import time

start = time.time()

number = 2**1000

num_str = str(number)

sum_ = 0
for i in range(0, len(num_str)):
  sum_ = sum_ + int(num_str[i])

elapsed = time.time() - start

print(sum_)
print(elapsed)
