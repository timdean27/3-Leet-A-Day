# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        

        hashMap = {}
        for i in range(len(t)):
            # Use the get() method to initialize the value to 0 if the key doesn't exist and add one if it exists or not
            hashMap[t[i]] = hashMap.get(t[i], 0) + 1


        left = 0
        right = 0
        minWindow = ""
        minLength = math.inf
        count = len(hashMap) # count of the letters we are searching for will decerement when we have found frequincy needed


        # Iterate with the right pointer
        for right in range(len(s)):
            # If s[right] is in the hashmap, decrease its frequency
            if s[right] in hashMap:
                hashMap[s[right]] -= 1
                # If we have found all occurrences of this character, reduce the count
                if hashMap[s[right]] == 0:
                    count -= 1
            
            # If all characters are matched at needed freqeuincy 
            # Try to shrink the window from the left
            while count == 0:
                # Update the minimum window if it's smaller than the current one
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    minWindow = s[left:right + 1]

                # Move the left pointer to shrink the window
                if s[left] in hashMap:
                    hashMap[s[left]] += 1
                    if hashMap[s[left]] > 0:
                        count += 1  # If a required character is missing, increment the count
                        # this will exit the while loop and use the for loop to increase right until needed letter is found again

                # while count remains zero , meaning all letters are still found we can shrink by moving left closer to right
                left += 1  # Shrink the window

            # Move the right pointer to expand the window

        return minWindow



sol = Solution()
print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC"))