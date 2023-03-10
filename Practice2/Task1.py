age = int(input("Enter your age:"))
License = input("Do you have a driving license?")

result = age >= 18 and License == "yes"

print("You are able to drive: " + str(result))
