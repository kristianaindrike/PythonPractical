#Task 5:Write a function that takes a list of integers and a target sum as parameters and 
#returns a list of two integers from the original list that add up to the target sum.

def pairs(integers,target_sum):
    seen = set()
    for number in integers:
        diff = target_sum - number
        if diff in seen:
            return [diff,number]
        seen.add(number)
    return []

number = [4,8,6,24,35,3,7,9]
target_sum = 27
print(pairs(number,target_sum))