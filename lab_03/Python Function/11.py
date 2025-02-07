import re 

def is_palindrome(s):
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned_s == cleaned_s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("No 'x' in Nixon"))