#Used permutation from itertools to permute over all the possible 3-lettered passwords. 
#The decrypted message was tested for the occurance of most common English words pulled out from a Wiki article.

#Answer = 129448
#Key = exp
#Message = An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum" 
#[On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum 
#of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this 
#series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series 
#is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal 
#to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this 
#series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, 
#the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. 
#Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 
#1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 
#90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar 
#reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.

#Time = 3.4829413890838623 s


import time
from itertools import permutations


def decrypt(secret_message):
	common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I"] #List of common English words taken from the Wikipedia article: 
	                                                                                #https://en.wikipedia.org/wiki/Most_common_words_in_English
	message_length = int(len(secret_message)/3)

	for key in permutations("abcdefghijklmnopqrstuvwxyz", 3):
		possible_message = ''.join(chr(data ^ ord(password)) for data, password in zip(secret_message, key*message_length))

		if all (possible_message.find(w) >= 0 for w in common_words):
			message = possible_message
			encryption_key = key 
	
	return message, encryption_key



start = time.time()

file_name = 'PE59.txt'
temp = open(file_name, 'r')
encrypted_message = temp.read()
encrypted_message = encrypted_message.split(',')
encrypted_message = [int(i) for i in encrypted_message]


decrypted_message, encryption_key = decrypt(encrypted_message)

key = ""

for i in range(0, len(encryption_key)):
	key += encryption_key[i] 


_sum = 0
for i in range(0, len(decrypted_message)):
	_sum += ord(decrypted_message[i])

elapsed = time.time() - start

print("Message = ",decrypted_message)
print("Key = ",key)
print(_sum)
print(elapsed)

