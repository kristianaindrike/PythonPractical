#Write the program to sort the list (without using sort function). You can implement any algorithm

list = [3,6,2,6,9,6,8,4,10,860,564,99,-1]
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list)
