#Task 2:Write a function that takes a string as a parameter and returns the number of vowels (aeiou) in the string.
# Hint: you can use given_character in "aeiou"

def count_vowels(text:str):
    text = text.lower()
    count = 0
    for letter in text:
        if letter in "aeiou":
            count += 1
    return count
textInp = input("Enter your text here: ")
print("There are " + str(count_vowels(textInp)) + " vowels in your text.")