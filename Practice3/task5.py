# Write a program that takes an integer as input and prints out whether that integer is prime or not.

number = int(input("Enter your number: "))
prime = True
if number <= 1:
    print(number, "is neither prime nor not prime number.")
else:
    for i in range (2,number):
            if (number % i) == 0:
                  prime = False
                  break
if prime == True:
     print(number,"is a prime number.")
else:
     print(number, "is not a prime number.")
