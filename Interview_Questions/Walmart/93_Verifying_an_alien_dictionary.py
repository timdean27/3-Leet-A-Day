# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character 


from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a mapping of each character to its rank in the alien alphabet
        order_map = {char: i for i, char in enumerate(order)}
        
        # Compare each word with the next one
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Compare characters of both words
            for k in range(min(len(word1), len(word2))):
                char1 = word1[k]
                char2 = word2[k]
                # If characters differ, decide order based on the alien dictionary
                if char1 != char2:
                    if order_map[char1] > order_map[char2]:
                        return False
                    break
            else:
                # If we exited the loop without finding a difference and word1 is longer
                if len(word1) > len(word2):
                    return False
        
        return True

# Examples
sol = Solution()
print(sol.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))  # Output: True
print(sol.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))  # Output: False
print(sol.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))  # Output: False
