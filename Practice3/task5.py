# Write a program that takes an integer as input and prints out whether that integer is prime or not.

number = int(input("Enter your number: "))
if number == 1:
    print(number, "is not a prime number.")
elif number > 1:
    for i in range (2,number):
            if (number % i) == 0:
                  print(number,"is not a prime number.")
else:
     print(number + "is prime number.")