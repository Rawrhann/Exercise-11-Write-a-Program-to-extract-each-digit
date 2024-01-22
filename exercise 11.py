#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = 7536
original_number = number


while number > 0:
    remainder = number % 10 

    number = number // 10
    print(remainder, end=" ")
