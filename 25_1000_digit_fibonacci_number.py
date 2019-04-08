#Easy peasy lemon squeezy

#Answer = 4782
#Time = 0.02752399444580078 s

import time

start = time.time()

a = 1
b = 1
index = 2
while len(str(b)) < 1000:
	c = a + b
	index += 1
	a = b
	b = c
    
elapsed = time.time() - start   
print(index)    
print(elapsed)