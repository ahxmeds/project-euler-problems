#Very easy in python since there exists a decimal-to-binary conversion routine

#Answer = 872187
#Time = 0.9896419048309326 s


import time


def is_palindrome(num):

  string_of_num = str(num)
  num_str_rev = ''
  
  length = len(string_of_num)
  for i in range(0, length):
    num_str_rev = num_str_rev + string_of_num[length - i -1] 

  if(string_of_num == num_str_rev):
    return True
  return False


start = time.time()

_sum = 0
for num in range(1, 1000001):
	if is_palindrome(num):
		bin_num = bin(num)
		binary_num = bin_num[2:len(bin_num)] #removing the first two characters '0b'
		if is_palindrome(binary_num):
			_sum += num 

elapsed = time.time() - start

print(_sum)
print(elapsed)

