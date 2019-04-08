# Using number of divisors formula 
# if prime factorization of n = p1^q1 p2^q2 ..... pk^qk, where p1, p2, ....., pk are prime factors of n
# then the number of divisors for this number is (q1+1)(q2+1).....(qk+1)

def number_of_divisors(n):
  if n%2 == 0: 
    n = n/2
  divisors = 1
  count = 0
  while n%2 == 0:
    count = count + 1
    n = int(n/2)
  divisors = divisors*(count+1)
  
  p = 3
  while n!=1:
    count = 0
    while n%p == 0:
      count = count + 1
      n = int(n/p)
    p = p + 2
    divisors = divisors*(count + 1) 
  return divisors
    

def triangle_index_with_N_divisors(N):
  n = 1
  factor1 = number_of_divisors(n)    #sum of natural numbers till n is n(n+1)/2
  factor2 = number_of_divisors(n+1)  # because n and n+1 are consecutive numbers, they do not have common 
                                     # prime numbers as their divisors
  while factor1*factor2 < N:
    n = n + 1
    factor1 = factor2
    factor2 = number_of_divisors(n+1)
  
  return n
  


n = triangle_index_with_N_divisors(500)
triangle_number = n*(n+1)//2

print(n, " ", triangle_number)
