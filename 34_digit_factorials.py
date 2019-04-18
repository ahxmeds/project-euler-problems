#The trick involved first finding an upper bound to the sum of the factorials of the digits which turned out to be 7x(9!).
#The runtime was decreased by storing the factorials already calculated in a dictionary.

#Answer = 40730
#Time = 5.065098762512207 s


import time

def factorial(n):
  if n == 0: return 1
  else: 
    return n*factorial(n-1)


#A function to return all the digits of a number n in an array
def get_digits(n):
  num_array = []	
  while(n > 0):
    num_array.append(n%10)
    n = n//10
  num_array.reverse()
  return num_array

start = time.time()

UPPER_LIMIT = 7*factorial(9)
_sum = 0
dictionary_of_factorials = {}
answer_numbers = []

for i in range(3, UPPER_LIMIT+1): # ignoring 1 and 2 since they are not sum (as given in problem statement)
  sum_i = 0
  digits_array = get_digits(i)

  for value in digits_array:
    if value in dictionary_of_factorials:
      sum_i += dictionary_of_factorials[value]
    else:
      dictionary_of_factorials[value] = factorial(value)
      sum_i += dictionary_of_factorials[value]
  
  if sum_i == i:
    _sum += i
    answer_numbers.append(i)

elapsed = time.time() - start

print(_sum)
print(answer_numbers)
print(elapsed)