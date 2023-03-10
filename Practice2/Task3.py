number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

number1Mod = number1 % 2
number2Mod = number2 % 2

#print(str(number1Mod))
#print(str(number2Mod))

print("Both numbers are even: ", number1Mod == 0 and number2Mod == 0)
print("At least one number is even: ", not (number1Mod != 0 and number2Mod !=0))