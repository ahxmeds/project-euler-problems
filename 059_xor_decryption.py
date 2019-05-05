import time


start = time.time()

file_name = 'PE42.txt'
names = open(file_name, 'r')
temp = names.read()
line = temp[1:-1]
words = line.split('\",\"')
