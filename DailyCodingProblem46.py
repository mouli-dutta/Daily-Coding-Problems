# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".


def longest_palindromic_substring(s):
    n = len(s)
    substrings = [s[i:j+1] for i in range(n) for j in range(i, n)]
    palindromes = filter(lambda x: x == x[::-1], substrings)
    return max(palindromes, key=len)


tests = ['aabcdcb', 'bananas']
print("\n".join(longest_palindromic_substring(test) for test in tests))
