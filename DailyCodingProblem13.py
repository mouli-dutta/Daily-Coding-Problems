# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def longest_substring_with_k_distinct_characters(s, k):
    left = 0
    right = 0
    max_length = 0
    max_start = 0
    max_end = 0
    char_set = set()
    
    while right < len(s):
        char_set.add(s[right])
        
        while len(char_set) > k:
            char_set.remove(s[left])
            left += 1
        
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_start = left
            max_end = right
        
        right += 1
    
    return s[max_start:max_end+1]


s = "abcba"
k = 2
print(longest_substring_with_k_distinct_characters(s, k))  # Output: "bcb"
