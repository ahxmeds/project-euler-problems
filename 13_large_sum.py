file_name = 'PE13.txt'

with open(file_name, "r") as fucking_large_number:
  array = []
  for line in fucking_large_number:
    array.append(line)

numbers = []

for i in array:
  numbers.append(int(i))

sum_ = 0

for i in numbers:
  sum_ = sum_ + i

sum_str = str(sum_)

print(sum_str[0:10])
