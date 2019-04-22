#For the identity, a x b = c, with a<=b the idea was finding the bounds on
#a and b so that number of digits in c do not exceed 9.
#Also, set function was used to make sure each product is counted only once.


#Answer = 45228
#Time = 0.8288247585296631 s 

import time

def is_pandigital(number):
  str_num = str(number)
  length = len(str_num)
  if length == 9:
    set_digits_ref = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    digits = []
    for i in range(0, len(str_num)):
      digits.append(int(str_num[i]))
    set_digits = set(digits)
    set_intersection = set_digits_ref & set_digits

    if set_intersection == set_digits_ref:
      return True
    else:
      return False
  else:
    return False


start = time.time()
answer_products = []

for a in range(1,100):
	for b in range(1,10000):
		prod = a*b
		concat = str(a) + str(b) + str(prod)
		if len(concat) == 9:
			if is_pandigital(int(concat)):
				answer_products.append(prod)

set_answer_products = set(answer_products)

_sum = sum(set_answer_products)
elapsed = time.time() - start

print(_sum)
print(elapsed)