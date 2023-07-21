#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

# Print the generated number
print("The string Last digit of {}, followed by".format(number))
print("the number {}, followed by".format(number))
print("the string is {}, followed by".format(str(number)[-1]))

# Check the last digit and print the corresponding message
last_digit = number % 10
if last_digit > 5:
    print("if the last digit is greater than 5: the string and is greater than 5")
elif last_digit == 0:
    print("if the last digit is 0: the string and is 0")
else:
    print("if the last digit is less than 6 and not 0: the string and is less than 6 and not 0")
