# Write a program that takes a user input (an integer) and determines whether it is positive,
# negative, or zero.

number = int(input("Enter your number: "))
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")