#Uses a prime checker and a permutation checker. Not the most efficient solution.

#Answer = 296962999629
#Time = 27.6352369785 s (checking until two such triplets are found)

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

#converting number to its individual digits array
def get_num_array(num):
	num_str = str(num)
	num_array = []
	for i in num_str:
		num_array.append(int(i))
	return num_array

#checking if num1 and num2 are permutations of each other
def is_permutation(num1, num2):
	num1_array = get_num_array(num1)
	num2_array = get_num_array(num2)
	if len(num1_array) != len(num2_array):
		return False
	else:
		numbers = [0,1,2,3,4,5,6,7,8,9]
		num1_dict = {}
		num2_dict = {}
	
		for i in numbers:
			num1_dict[i] = 0
			num2_dict[i] = 0
		for i in num1_array:
			num1_dict[i] += 1		
		for i in num2_array:
			num2_dict[i] += 1
	
		if num1_dict == num2_dict:
			return True
		else: 
			return False


start = time.time()  
prime_list = [] #list to store all 4-digit primes 
for i in range(1000,10000):
	if is_prime(i) == True:
		prime_list.append(i)

triplets = [] #list to store of the possible triplets
flag = 0 #flag to signal the 2nd triplet found
for i in range(0, len(prime_list)):
	for j in range(i, len(prime_list)):
		for k in range(j, len(prime_list)):
			a = prime_list[i]
			b = prime_list[j]
			c = prime_list[k]
			if c - b == b - a and a < b and b < c: #checking if the sequence in the triplet is increasing and by same amount 
				if is_permutation(a, b) == True and is_permutation(a, c) == True and is_permutation(b, c) == True: #checking for "permutativity"
					triplets.append([a, b, c])
					print(str(a) + "\t" + str(b) + "\t" + str(c)+"\n") #printing the required triplets
					if len(triplets) == 2:
						flag = 1
						break
		if flag == 1:
			break
	if flag == 1:
		break

answer = int(str(triplets[1][0]) + str(triplets[1][1]) + str(triplets[1][2]))
print(answer)
elapsed = time.time() - start
print(elapsed)
