import sys

s= sys.argv[1]

if s == s[::-1]:
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")
