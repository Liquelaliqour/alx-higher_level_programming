#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lno = abs(number) % 10
if number < 0:
    lno *= -1
if lno != 0 and lno > 5:
    print("Last digit of", number, "is", lno, "and is greater than 5")
elif lno == 0:
    print("Last digit of", number, "is", lno, "and is 0")
elif lno != 0 and lno < 6:
    print("Last digit of", number, "is", lno, "and is less than 6 and not 0")
elif lno != 0 and lno < 0:
    print("Last digit of", number, "is", lno, "and is less than 6 and not 0")
# YOUR CODE HERE is an amazing code 
