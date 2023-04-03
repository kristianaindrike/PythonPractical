#Task 4:Write a function that takes a list of integers as a parameter and returns a list of only the even 
#integers in the original list

def even_integers(listInput:list):
    evenList = []
    for element in listInput:
        if element % 2 == 0:
            evenList.append(element)
    return evenList

listInp = [3,5,7,2,55,6,7,32,4,8,97,0,1]
print(even_integers(listInp))