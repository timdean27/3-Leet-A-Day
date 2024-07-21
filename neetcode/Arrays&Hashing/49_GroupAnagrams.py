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
 
# Importing defaultdict from the collections module.
# defaultdict allows us to create a dictionary that provides a default value for the key that does not exist.
from collections import defaultdict
# Importing List from the typing module to specify the type of list elements.
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Creating a defaultdict of lists to store anagrams.
        anagrams = defaultdict(list) 
        # Looping through each string in the input list.
        for s in strs:
            # Sorting the string and using the sorted string as a key in the dictionary.
            sorted_str = ''.join(sorted(s))
            # Appending the original string to the list corresponding to the sorted key.
            anagrams[sorted_str].append(s)    
        # Returning the values of the dictionary as a list of lists.
        return list(anagrams.values())
    
# Creating an instance of the Solution class.
sol = Solution()
ans = sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])

print(ans)
