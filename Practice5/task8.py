#Task 8:Write a function that takes a dictionary as a parameter and returns a list of all the keys in the 
#dictionary that have an even value.

def key_of_even(dict_list:dict):
    keys = []
    for key,value in dict_list.items():
        if value % 2 == 0:
            keys.append(key)
    return keys

input_dict = {"1":6, "2":10, "3":7, "4":9}
print(key_of_even(input_dict))