for a in range(1, 998):
  for b in range(a+1, 999):
    for c in range(b+1, 1000):
      if(a*a + b*b == c*c):
         if(a + b + c == 1000):
            print(a,"  ", b, " ", c)
            product = a*b*c


print(product)
