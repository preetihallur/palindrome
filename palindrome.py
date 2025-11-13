# palindrome_check.py
# Program to check if a given string is a palindrome
import sys
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]
    
    user_input = sys.argv[1]
    if s==user_input:
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")
