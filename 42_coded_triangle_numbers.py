#Answer = 162
#Time = 0.0026290416717529297 s

import time
import math as m

def word_score(word):
	score = 0
	for i in range(0, len(word)):
		score = score + ord(word[i])
	score = score - 64*len(word)
	return score


def is_triangle_number(number):
	#solving the quadratic equation n^2 + n -2(number) = 0

	n = (-1 + m.sqrt(8*number + 1))/2

	floor_n = m.floor(n)
	if floor_n == n:
		if (n*(n+1))/2 == number:
			return True
	else:
		return False

def is_triangle_word(word):

	word_value = word_score(word)
	if is_triangle_number(word_value):
		return True
	else:
		return False


start = time.time()

file_name = 'PE42.txt'
names = open(file_name, 'r')
temp = names.read()
line = temp[1:-1]
words = line.split('\",\"')

count = 0
triangle_words = []

for word in words:
	if is_triangle_word(word):
		count += 1
		triangle_words.append(word)


elapsed = time.time() - start
print(count)
print(triangle_words)
print(elapsed)
