def is_palindrome(num):

  string_of_num = str(num)
  num_str_rev = ''
  
  length = len(string_of_num)
  for i in range(0, length):
    num_str_rev = num_str_rev + string_of_num[length - i -1] 

  if(string_of_num == num_str_rev):
    return True
  return False


max = 1

for i in range(100, 1000):
  for j in range(100, i):
    product = i*j
    if (is_palindrome(product)):
      if(product > max):
        max = product
      


print(max)
