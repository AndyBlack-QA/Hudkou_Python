# Task
# Make up an algorithm
# If the entered number is greater than 7, then print “Hello”
# If the entered name matches “John”, then output “Hello, John”, if not, then output "There is no such name"
# There is a numeric array at the input, it is necessary to output array elements that are multiples of 3


entered_number = int(input("Enter any number"))  # Enter the number

if entered_number > 7:  #Check if number greater than 7
    print("Hello")  # If number more than 7 print "Hello"
else:
    print("I can't say Hello to you")  # Here I handle the situation if number less or equal to 7

entered_name = str(input("Enter your name"))  # Enter the name

if entered_name.strip() == 'John':  #Check if name "John"
    print("Hello, John")  # If name is John then print "Hello, John"
else:
    print("There is no such name")  #If name is not a John, then print "There is no such name"

entered_numbers = input("Enter numbers separated by spaces: ")  # Enter numbers
numeric_list = [int(x) for x in entered_numbers.split()]  # Make a list of entered numbers by splitting them by spaces,
# using method split without a separator, by default if split by a space
multiplied_list = [num * 3 for num in numeric_list]  #go through every element and multiply it by 3

print(multiplied_list) #print the final result where all original numbers multiplied by 3
