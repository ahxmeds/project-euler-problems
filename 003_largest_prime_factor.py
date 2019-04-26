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
  #for i in range(3, int(m.sqrt(num))+1, 2):
   # if(number%i == 0):
    #  return False
  return True


#makes list of all factors and returns the 
def prime_factors(number):
  divisor_list = []
  LPF = number

  for i in range(2, int(m.sqrt(number))):
    if(number%i == 0 and is_prime(i) == True):
      divisor_list.append(i)
  LPF = divisor_list.pop()
  return LPF


num = 600851475143

answer = prime_factors(num)
print("The answer is : ", answer)
