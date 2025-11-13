# palindrome_check.py
# Program to check if a given string is a palindrome
import sys
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]

if __name__ == "__main__":
    user_input = sys.argv[1]
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")
