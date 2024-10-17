# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # make a stack with the smaller string 
        # input string in reverce order so we can get the last value and pop it out if i matchs
        if len(text1) >= len(text2):
            shortString = text2
            longString = text1
        else:
            shortString = text1
            longString = text2

        stack = []
        for i in range(len(shortString)):
            stack.append(shortString[len(shortString)-(1+i)])

        print(stack)
        print(stack[-1])
        # check the current value of longer string vs the recent last value of stack 
        # if matching pop out of stack and increase count by 1
        maxCount = 0

        while(len(stack) > 0):
            tempStack = stack.copy()
            count = 0
            for letter in longString:
                # Check if tempStack has elements before comparing
                if tempStack and letter == tempStack[-1]:
                    tempStack.pop()
                    count += 1

            maxCount = max(maxCount , count)
            stack.pop()
        
        return maxCount
    
sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))  # Expected output: 3
print(sol.longestCommonSubsequence("abc", "abc"))    # Expected output: 3
print(sol.longestCommonSubsequence("abc", "def"))    # Expected output: 0