# Good morning! Here's your coding interview problem for today.

# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        
class AutocompleteSystem:
    def __init__(self, dictionary):
        self.root = TrieNode()
        for word in dictionary:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def search(self, query):
        node = self.root
        for char in query:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_all_words(node, prefix=query)

    def _get_all_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words += self._get_all_words(child_node, prefix=prefix + char)
        return words


#test
dictionary = ['dog', 'deer', 'deal', 'doe', 'doll']
autocomplete = AutocompleteSystem(dictionary)
results = autocomplete.search('de')
print(results)  # Output: ['deer', 'deal']
