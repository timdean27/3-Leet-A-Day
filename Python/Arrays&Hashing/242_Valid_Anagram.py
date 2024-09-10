# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


class Solution(object):
    def isAnagram(self, s, t):
        
        sSort = ''.join(sorted(s))
        tSort = ''.join(sorted(t))
        print(sSort, tSort)
        return sSort == tSort


run = Solution()

print(run.isAnagram(s = "anagram", t = "nagaram"))
        