#Generating an array of primes below 1-million
#then scanning and summing the array elements with given start and end indices (loop breaks when sum > 1-million)
#at which point, the variable end is also fixed. At any point, if the sum of consective prime is of span = x, the 
#next secondloop index starts from firstloop index + x.   

#Answer = 997651
#Time = 15.341108322143555 s 

import time 

#check whether prime or not
def is_prime(number):
  if number <=1: return False
  elif number == 2: return True
  elif number%2 == 0: return False
  i = 3
  while (i*i <= number):
    if number%i == 0:
      return False
    i = i+1
  return True


#generates an array of all the primes below the given number, cutoff.
def generate_prime_array(cutoff):
    prime_array = []
    for i in range(2, cutoff):
        if is_prime(i) == True:
            prime_array.append(i)
    return prime_array


start = time.time()

CUT_OFF = 1000000
prime_array = generate_prime_array(CUT_OFF)
span = 0
end = len(prime_array)
max_prime = 0

for i in range(0, len(prime_array)):
	for j in range(i + span, end):
		summ = sum(prime_array[i:j])
		if summ < CUT_OFF:
			if summ in prime_array:
				max_prime =  summ 
				span = j - i
		else:
			end = j + 1
			break

print(max_prime)
elapsed = time.time() - start
print(elapsed)