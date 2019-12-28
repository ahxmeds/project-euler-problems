#incomplete: hard problem


import time
import math as m

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

#returns all the wildcards for a given number. eg. for 11, it returns [*1, 1*, **]  
def get_wildcard_list(number):
	num_str = str(number)
	ndigits = len(num_str)
	total_elements_in_WC_list = 2**ndigits - 1
	WC_array = []
	for ele_replace in range(1, ndigits+1):
		string = 



#does all types of replacements, i.e., 1-digit, 2-digits, etc 
def generate_wildcard_dictionary(number, prime_array):
	prime_WC_dict = {}



CUT_OFF = 1000000
prime_array = generate_prime_array(CUT_OFF)

family_size = 0

while family_size < 8:
	replace_digits()
