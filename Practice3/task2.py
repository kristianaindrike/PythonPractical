# Write a program that prints out the numbers from 1 to 100. But for multiples of three, print "Fizz" 
# instead of the number and for multiples of five, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".

seq = range(1,101)
for i in seq:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    
    