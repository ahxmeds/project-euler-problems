#There could be other longer traversal-based implementations of this problem. 
#Here, I solve the problem combinatorially. I denote a right_motion as 1 and a down-motion as 0. 
#For finding the number of path on an NxN grid, the problem reduces 
#to the number of ways N 1's and N 0's can be arranged in a line. 
#Each unique permutation gives a unique path.

#Answer = 137846528820
#Time =  1.811981201171875e-05 s

def factorial(n):
  if n == 0: return 1
  else: 
    return n*factorial(n-1)
  

import time

start = time.time()

grid_size = 20

paths = int(factorial(2*grid_size)/(factorial(grid_size)*factorial(grid_size)))


elapsed = time.time() - start

print(paths)
print(elapsed)
