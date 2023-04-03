#Task 3:Write a function that takes a string as a parameter and returns True if the string is a palindrome and 
#False otherwise.

def reverse(text:str):
    revStr = ""
    for char in text:
        revStr = char + revStr
    return revStr

def is_palindrome(text:str):
    if reverse(text) == text:
        return True
    else:
        return False
textInp = input("Enter your text: ")
print(is_palindrome(textInp))