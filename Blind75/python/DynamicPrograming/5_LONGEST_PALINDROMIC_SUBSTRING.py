# 5. Longest Palindromic Substring

# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        longestSub = ''
        
        def checkPalindrome(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        for i in range(len(s)):
            #odd length
            left ,right = i , i 
                      # starting from single character "cabac"
            odd_palindrome = checkPalindrome(left, right)
            # starting from a pair of characteres example "cabbac"
            even_palindrome = checkPalindrome(left, right + 1)

            
            # Update the longest palindrome found so far
            if len(odd_palindrome) > len(longestSub):
                longestSub = odd_palindrome
            if len(even_palindrome) > len(longestSub):
                longestSub = even_palindrome
        return longestSub

sol = Solution()
print(sol.longestPalindrome(s = "babad"))