import time

start = time.time()

#First solution took 39.68187165260315 seconds to complete
'''
max_count = 0

for i in range(1, 1000001):
  print(i)
  count = 0
  current_num = i
  while current_num > 1:
    if(current_num%2 == 0):
      current_num = current_num/2
    else:
      current_num = 3*current_num + 1
    count = count + 1
  if count > max_count:
    max_count = count
    number = i
'''

#A more efficient solution - here I saved the lengths of already calculated numbers in a dictionary. A great improvement-- took only 8.295971155166626 seconds.

collatz_dictionary = {}

def collatz(n):
  sequence = []
  sequence.append(n)
  current_num = n
  while current_num > 1:
    if(current_num%2 == 0):
      current_num = current_num/2
      if current_num in collatz_dictionary:
        sequence = sequence + collatz_dictionary[current_num]
        break
      else:
        sequence.append(current_num)
    else:
      current_num = 3*current_num + 1
      if current_num in collatz_dictionary:
         sequence = sequence + collatz_dictionary[current_num]
         break
      else: 
         sequence.append(current_num)
  
  collatz_dictionary[n] = sequence
  return len(sequence)


max_length = 0

for i in range(1000000):
  length = collatz(i)
  if length > max_length:
    max_length = length
    number = i

elapsed = time.time() - start
print(number, " ", elapsed)

