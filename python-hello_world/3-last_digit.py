import random
number = random.randint(-10000, 10000)
counter=0
limit=  -10000
last_digit=(number) % 10
if  last_digit > 5 : 
  print(number,'is positive')
if last_digit == 0: 
  print(number,'is zero')
if last_digit < 6 !=0:
  print(number,'is negative')