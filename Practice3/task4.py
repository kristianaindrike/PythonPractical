#Create calculator: Ask user to provide 2 numbers and one operation to be performed 
# (*,/,+.- or %). If the operation provided does not match one of these, the program should print 
# "Operation provided isn't valid, please,try again" - in this case, the program should ask for 
# the operation to be provided again.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter one of the operations * , / , + , - , %: ")
if operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
else:
    print("Operation provided isn't valid, please try again")