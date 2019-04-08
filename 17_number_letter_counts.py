#Most of the time spent in making the dictionary
#Answer = 21124
#Time = 0.0071544647216796875 s

import time

start = time.time()

dictionary = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
 100: 'hundred',
 1000: 'onethousand'
  }


letter_count = ""

for i in range(1, 1001):
  current_num = str(i)
  if len(current_num) == 1:
       letter_count += dictionary[int(current_num)]
       print(dictionary[int(current_num)])
    
  elif len(current_num) == 2:
    if ((int(current_num)>=10 and int(current_num)<=20) or int(current_num) == 30 or int(current_num) == 40 or int(current_num) == 50 or int(current_num) == 60 or int(current_num) == 70 or int(current_num) == 80 or int(current_num) == 90):
       letter_count += dictionary[int(current_num)]
       print(dictionary[int(current_num)])
    else:
       num = int(current_num)
       tens_digit = num//10
       ones_digit = num%10
       letter_count += dictionary[tens_digit*10] + dictionary[ones_digit]
       print(dictionary[tens_digit*10] + dictionary[ones_digit])
  
  elif len(current_num) == 3:
    if int(current_num) == 100:
       letter_count += "one" + dictionary[100]
       print("one" + dictionary[100])
    elif(int(current_num)%100 == 0):
       letter_count += dictionary[int(current_num)//100] + dictionary[100]
       print(dictionary[int(current_num)//100] + dictionary[100])
    else: 
       num = int(current_num)
       hundreds_digit = num//100
       last_2_digits = num%100
       tens_digit = last_2_digits//10
       ones_digit = last_2_digits%10
       if(tens_digit == 1):
         letter_count += dictionary[hundreds_digit] + dictionary[100] + 'and' + dictionary[tens_digit*10 + ones_digit] 
         print(dictionary[hundreds_digit] +  dictionary[100]+ 'and'+  dictionary[tens_digit*10 + ones_digit])
       else:
         letter_count += dictionary[hundreds_digit] + dictionary[100] + 'and' + dictionary[tens_digit*10] + dictionary[ones_digit]
         print(dictionary[hundreds_digit] + dictionary[100] +'and' + dictionary[tens_digit*10] + dictionary[ones_digit])
  else:
       letter_count += dictionary[1000]
       print(dictionary[int(current_num)])
elapsed = time.time() - start
#print(letter_count)
print(len(letter_count))
print(elapsed)
