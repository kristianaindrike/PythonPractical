#Task 6: Write a function that takes a list of integers as a parameter and returns the product of all the 
#integers in the list.

def product_of_list(numbers:list):
    product = 1
    for number in numbers:
        product += number
    return product
numbers = [2,4,6,8,11,5]
print(product_of_list(numbers))
