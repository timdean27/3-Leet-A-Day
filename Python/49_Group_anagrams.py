# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(strs)
        group = {}
        for word in strs:
            breakwords = sorted(word)
            print(breakwords)
            sorted_word = ''.join(breakwords)
            print(sorted_word)
            if sorted_word in group:
                group[sorted_word].append(word)
            else:
                group[sorted_word] = [word]

            # Convert the values of the dictionary to a list of lists
            result = list(group.values())
    
sol = Solution()

# Call the isPalindrome method
result = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)

