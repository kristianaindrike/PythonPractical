#Write a program that takes an integer as input and prints out all the factors of that integer.

number = int(input("Enter number: "))
for i in range(1,number + 1):
    if number % i == 0:
        print(i)