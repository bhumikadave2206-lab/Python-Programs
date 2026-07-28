# (33) Palindrome Check
#we can use the string slicing reverse rule in this so we can easily do the programe to check palindrome or not 
# in python this is very easy programe to check plaindrome 
#but in some other language itt gone somthing tricky

def is_palindrome(s):
 return s == s[::-1]
print(is_palindrome("madam"))
print(is_palindrome("racecar"))