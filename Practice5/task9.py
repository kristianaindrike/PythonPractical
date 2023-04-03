#Task 9:Write a function that takes a list of dictionaries as a parameter and returns a new dictionary 
#that contains the sum of the values for each key in the original dictionaries.

def get_sum(list_of_dict:list):
    sum_dict = dict()
    for values_dict in list_of_dict:
        sum = 0
        for key,value in values_dict.items():
            if key in sum_dict:
                sum = sum_dict.get(key)
                sum += value
                sum_dict[key] = sum
            else:
                sum_dict[key] = value
    return sum_dict

listInput = [{1:19,2:7,3:9},{1:21,2:1,3:10},{1:4,2:6,3:8}]
print(get_sum(listInput))
