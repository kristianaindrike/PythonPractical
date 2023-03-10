day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

valid = day > 0 and day < 32 and month > 0 and month < 13

print(valid)