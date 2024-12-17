# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if lengths are different
        if len(s) != len(t):
            return False
        
        hashMap = {}
        # Count the frequency of characters in the first string 's'
        for char in s:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1

        for char in t:
            if char in hashMap:
                hashMap[char] -= 1
                # If any character count goes below 0, it's not an anagram
                if hashMap[char] < 0:
                    return False
            else:
                return False
        return True
                