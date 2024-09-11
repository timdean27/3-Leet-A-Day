# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a DP array with the size of the string plus one.
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: An empty string can always be segmented.
        
        for i in range(len(wordDict[i])):
            for j in range(dp[i], len(s)):
                if letter[j] == wordDict[i][j]:
                    dp[i] = j


sol = Solution()
print(sol.wordBreak(s = "leetcode", wordDict = ["leet","code"]))