"""Demonstrates how to count something"""

number_string: str = "321"
number_of_odd: int = 0

# if a number % 2 ==1, then it is odd
if (int(number_string[0]) % 2 == 1):
    number_of_odd = number_of_odd + 1
if (int(number_string[1]) % 2 == 1):
    number_of_odd = number_of_odd + 1
if (int(number_string[2]) % 2 == 1):
    number_of_odd = number_of_odd + 1

print("You have " + str(number_of_odd) + "in the string!") 
