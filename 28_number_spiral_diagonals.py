#A slower implementation will be creating the entire NxN matrix of spiral numbers
#and finding the sum of both the diagonals. In this implementation, I have used a
#cleverer trick by finding a pattern in the numbers that need to be summed.

#Let e_i and o_i be the i^{th} even and odd numbers respectively.
#For n = 500, for the main diagonal:
    #the top-right sum = \sum_{(2i+1)^2}, with i = 0...n (includes 1)
    #the bottom-left sum = \sum_{(2i)^2 + 1}, with i = 1...n 
#For n = 500, for the off-diagonal:
    #the top-left sum = \sum{(2i)^2 + 2i + 1}, with i = 1...n
    #the bottom-right sum = \sum{(2i+1)^2 + (2i+1) + 1}, with i = 0...n


#Answer = 669171001
#Time = 0.0007228851318359375 s

import time

start = time.time()

side = 1001
sum_ = 0

for i in range(1, side+1):
	if i%2 == 0:
		sum_ += (i**2) + 1
		sum_ += (i**2) + i + 1
	else:
		sum_ += i**2
		sum_ += (i**2) + i + 1

sum_ -= (i**2) + i + 1  #subtracting the last number from the bottom-right corner which is not present in the spiral

elapsed = time.time() - start

print(sum_) 
print(elapsed)  
  