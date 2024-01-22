#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = 7536
original_number = number
print("original number is", number)

reverse_number = 0
count = 0
while number > 0:
    remainder = number % 10 
    reverse_number = (reverse_number * 10) + remainder
    number = number // 10
    count = count + 1

reverse_number_string = str(reverse_number)
for i in range(0, count, 1):
    print(reverse_number_string[i], end=" ")
