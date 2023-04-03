#Task 10:Write a function that takes a tuple as a parameter and returns a new tuple that has the first and 
#last elements swapped.

def rev_tuple(tup:tuple):
    tup_list = list(tup)
    tup_list[0],tup_list[len(tup_list)-1] = tup_list[len(tup_list)-1],tup_list[0]
    return tuple(tup_list)

Input_tup = (34,67,35,85,24,5)
print(rev_tuple(Input_tup))