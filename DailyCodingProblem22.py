# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces), 
# return the original sentence in a list. 
# If there is more than one possible reconstruction, return any of them. 
# If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


def word_break(s, word_dict):
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for i in range(start, len(s)):
            prefix = s[start:i+1]
            if prefix in word_dict:
                path.append(prefix)
                backtrack(i+1, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result[0] if result else None

# Example usage
word_dict1 = {'quick', 'brown', 'the', 'fox'}
s1 = 'thequickbrownfox'
print(word_break(s1, word_dict1))

word_dict2 = {'bed', 'bath', 'bedbath', 'and', 'beyond'}
s2 = 'bedbathandbeyond'
print(word_break(s2, word_dict2))