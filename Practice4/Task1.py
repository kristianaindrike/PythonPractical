# Ask the user to enter the text and a letter. Count how many occurrences of the letter provided. 

import re
text = input("Enter text: ")
letter = input("Enter a letter: ")
match = re.search(letter, text)
count = text.count(letter)
if match:
    print("Match found "+str(count)+" times.")
else: 
    print("Match not found!")

# Based on the task 1, count the occurrences of each character in the text provided and 
# display them in the output

occurrances = set(text)
for element in occurrances:
    countOfChar = 0
    for character in text:
        if character == element:
            countOfChar += 1
    print("Count of character '{}' is {}".format(element,countOfChar))