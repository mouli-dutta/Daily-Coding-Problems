# Good morning! Here's your coding interview problem for today.

# This problem was asked by Quora.

# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

# As another example, given the string "google", you should return "elgoogle".

def make_palindrome(s):
    if len(s) <= 1:
        return s
    
    elif s[0] == s[-1]:
        return s[0] + make_palindrome(s[1:-1]) + s[-1]
    
    else:
        # recursively insert character at the beginning
        palindrome1 = s[0] + make_palindrome(s[1:]) + s[0]
        # recursively insert character at end
        palindrome2 = s[-1] + make_palindrome(s[:-1]) + s[-1]

        # return the shortest 
        if len(palindrome1) < len(palindrome2):
            return palindrome1
        elif len(palindrome2) < len(palindrome1):
            return palindrome2
        
        # or lexicographically earliest 
        else:
            return min(palindrome1, palindrome2)


tests = ["race", "google", "car", "abab", "aaaaa"]

for test in tests:
    print(make_palindrome(test))
    