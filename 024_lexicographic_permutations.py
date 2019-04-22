#Based on the lexicographic permutation generation algorithm presented in the book, 
#"The Art of Computer Programming, Generating All Tuples and Permutations" by Donald Knuth.

#Answer = 2783915460
#Time = 5.497802257537842 s (when generating till millionth permutation is reached)
#Time1 = 22.275930166244507 s (when generating all the possible permuations)

import time

def factorial(n):
  if n == 0: return 1
  else: 
    return n*factorial(n-1)


start = time.time()    

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation_dictionary = {}


permutation_dictionary[1] = ''.join(str(i) for i in num)

total_permutations = factorial(len(num)) #can use this in the for loop below for calculating all the permutations 
                                         #lexicographic order
till_N = 1000000 #using this for lower runtime

for count in range(2, till_N+1):
  max_k = 0	
  for k in range(0, len(num)-1):
    if num[k] < num[k+1]:
      if k > max_k:
        max_k = k

  
  max_l = max_k
  for l in range(max_k + 1, len(num)):
      if num[l] > num[max_k]:
        if l > max_l:
          max_l = l
    
  num[max_k], num[max_l] = num[max_l], num[max_k] #python swap

  num[max_k+1:len(num)] = reversed(num[max_k+1:len(num)])
  permutation_dictionary[count] = ''.join(str(i) for i in num)
  #print(str(i) + " : " + str(permutation_dictionary[i]))

elapsed = time.time() - start
    
print(permutation_dictionary[1000000])
print(elapsed)
