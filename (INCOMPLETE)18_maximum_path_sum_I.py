import time

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

max_sum = 0

while True













elapsed = time.time() - start


print(elapsed)
