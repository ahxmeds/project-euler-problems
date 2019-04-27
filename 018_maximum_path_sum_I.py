#The order to reach the bottom of the tree, on needs to start at the top and at each step, either move to left (denoted by 0)
#or move right (denoted by 1). Hence, any path from top to bottom can be represented using a string of 0s and 1s, and there are 
#2^14 such permutations that are generated via a function. Hence, all 2^14 paths are checked to find the maximum sum.
#Path leading to maximum sum is found to be 11001001111101 (75->64->82->87->82->75->73->28->83->32->91->78->58->73->93)


#Answer = 1074
#Time = 0.10083460807800293 s

import time


def generate_all_permutations_to_reach_bottom():
	perm = []
	for i1 in range(0,2):
		for i2 in range(0,2):
			for i3 in range(0,2):
				for i4 in range(0,2):
					for i5 in range(0,2):
						for i6 in range(0,2):
							for i7 in range(0,2):
								for i8 in range(0,2):
									for i9 in range(0,2):
										for i10 in range(0,2):
											for i11 in range(0,2):
												for i12 in range(0,2):
													for i13 in range(0,2):
														for i14 in range(0,2):
															current = str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)+str(i10)+str(i11)+str(i12)+str(i13)+str(i14)
															perm.append(current)
	return perm

start = time.time()

file_name = 'PE18.txt'

with open(file_name, "r") as triangle:
  array = []
  for line in triangle:
    array.append(line.rstrip("\n"))

numbers = []

for i in array:
  row = i.split(" ")
  numbers.append(row)

numbers = [[int(i) for i in j] for j in numbers]

permutations = generate_all_permutations_to_reach_bottom()
max_sum = 0

for pattern in permutations:
	row, column = 0, 0
	_sum = numbers[row][column]
	for i in range(0, len(pattern)):
		if pattern[i] == '0':
			row += 1
			_sum += numbers[row][column]
		elif pattern[i] == '1':
			row += 1
			column += 1
			_sum += numbers[row][column]
	if _sum > max_sum:
		max_sum = _sum
		max_pattern = pattern

elapsed = time.time() - start

print(max_sum)
print(max_pattern)
print(elapsed)
