import time

def sum_calculator(x1, x2, x3, x4, x5, x6, x7, x8):
	return x1 + 2*x2 + 5*x3 + 10*x4 + 20*x5 + 50*x6 + 100*x7 + 200*x8

count = 0
for x1 in range(0, 201):
	for x2 in range(0, 101):
		for x3 in range(0, 41):
			for x4 in range(0, 21):
				for x5 in range(0, 11):
					for x6 in range(0, 5):
						for x7 in range(0,3):
							for x8 in range(0, 2):
								if sum_calculator(x1, x2, x3, x4, x5, x6, x7, x8) == 200:
									count += 1
									print(count)

print(count)