#The trick involved first finding an upper bound to the sum of the fifth power of the digits which turned out to be 6x(9^4).
#The runtime improved by storing the ffith powers already calculated in a dictionary.

#Answer = 443839
#Time = 0.6281273365020752 s


import time

def fifth_power(n):
  return n**5

#A function to return all the digits of a number n in an array
def get_digits(n):
  num_array = []	
  while(n > 0):
    num_array.append(n%10)
    n = n//10
  num_array.reverse()
  return num_array

start = time.time()

UPPER_LIMIT = 6*fifth_power(9)
_sum = 0
dictionary_of_fifth_powers = {}
answer_numbers = []

for i in range(2, UPPER_LIMIT+1):
  sum_i = 0
  digits_array = get_digits(i)

  for value in digits_array:
    if value in dictionary_of_fifth_powers:
      sum_i += dictionary_of_fifth_powers[value]
    else:
      dictionary_of_fifth_powers[value] = fifth_power(value)
      sum_i += dictionary_of_fifth_powers[value]
  
  if sum_i == i:
    _sum += i
    answer_numbers.append(i)

elapsed = time.time() - start

print(_sum)
print(answer_numbers)
print(elapsed)