#Answer = 4075
#Time = 0.08497810363769531 s


import time

def factorial(n):
  if n == 0: return 1
  else: 
    return n*factorial(n-1)

def n_choose_r(n, r):
	if n < r:
		print("Invalid entries")
	else:
		return factorial(n)/(factorial(n-r)*factorial(r))

start = time.time()

count = 0

for n in range(1, 101):
	for r in range(0, n):
		if n_choose_r(n, r) > 1000000:
			count += 1

elapsed = time.time() - start

print(count)
print(elapsed)