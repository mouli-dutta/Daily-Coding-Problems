# Good morning! Here's your coding interview problem for today.

# This problem was asked by Palantir.

# Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand side with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

import textwrap

def justify_text(words, k):
    # Join the words into a single string with spaces in between
    text = " ".join(words)
    
    # Use textwrap to split the text into lines and justify each line
    lines = textwrap.fill(text, width=k, replace_whitespace=False).split("\n")
    
    # Replace placeholders with the appropriate number of spaces
    for i, line in enumerate(lines):
        line = line.replace("\x00", "")
        words = line.split()
        num_spaces = k - sum(len(word) for word in words)
        num_gaps = len(words) - 1
        if num_gaps == 0:
            lines[i] = line.replace(" ", " " * num_spaces)
        else:
            spaces_per_gap = num_spaces // num_gaps
            extra_spaces = num_spaces % num_gaps
            for j in range(num_gaps):
                words[j] += " " * spaces_per_gap
                if j < extra_spaces:
                    words[j] += " "
            lines[i] = " ".join(words)
    
    return lines


# test
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

print(justify_text(words, k))
