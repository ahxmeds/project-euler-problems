#Very easy to solve in python. 
#Just figure out the maximum natural number so that you cross the 1000000th position.

#Answer = 210
#Time = 0.058148860931396484 s

import time

start =time.time()

string = ""
for num in range(1,199999):
	string += str(num)

dig_1 = int(string[0])
dig_10 = int(string[9])
dig_100 = int(string[99])
dig_1000 = int(string[999])
dig_10000 = int(string[9999])
dig_100000 = int(string[99999])
dig_1000000 = int(string[999999])

product = dig_1*dig_10*dig_100*dig_1000*dig_10000*dig_100000*dig_1000000
elapsed = time.time() - start

print(product)
print(elapsed)