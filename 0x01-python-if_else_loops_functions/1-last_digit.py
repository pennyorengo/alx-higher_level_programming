#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
print("Last digit of", number, "is", last_digit,"\n")
if last_digit > 5:
    print("and is greater than 5\n")
elif last_digit == 0:
    print("and is 0\n")
else:
    print("and is less than 6 and not 0\n")
