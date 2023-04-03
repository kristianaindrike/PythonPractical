#Task 11:Write a function that takes a set as a parameter and returns a new set that contains only the elements 
#that are not divisible by 3.

def non_div_3(input_set:set):
    non_div_3_set = set()
    for element in input_set:
        if element % 3 != 0:
            non_div_3_set.add(element)
    return non_div_3_set

inp_set = {5,7,3,2,9,56}
print(non_div_3(inp_set))