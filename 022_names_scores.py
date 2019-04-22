#Idea used is fetching the ASCII code of the alphabet characters using ord()

#Answer = 871198282
#Time = 0.0065174102783203125 s


import time

def word_score(word):
  score = 0
  for i in range(0, len(word)):
    score = score + ord(word[i]) - 64
  
  #score = score - 64*len(word)
  return score
  

start = time.time()

file_name = 'PE22.txt'

names = open(file_name, 'r')
temp = names.read()
line = temp[1:-1]
words = line.split('\",\"')
  
sorted_words = sorted(words)
total_score = 0

for i in range(0, len(sorted_words)):   	
  total_score = total_score + (i+1)*word_score(sorted_words[i])
  
elapsed = time.time() - start

print(total_score)
print(elapsed)
