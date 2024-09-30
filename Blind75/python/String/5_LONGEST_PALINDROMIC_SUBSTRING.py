
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
        # for planindroms it is ofetn usefull to expaind outwards from center 
        #  eample cabac if we start b we know char[b-1] must == char[b+1] for it to be valid palindrome

        longest = ''
        # helper function to check for palandrom
        def isPalindrome(left,right):
            # check that left and right are inbounds and that left and right are equal if not then its not palindrom and dont need to continue
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            # starting from single character "cabac"
            odd_palindrome = isPalindrome(i, i)
            # starting from a pair of characteres example "cabbac"
            even_palindrome = isPalindrome(i, i + 1)

            
            # Update the longest palindrome found so far
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

sol = Solution()
print(sol.longestPalindrome(s = "babad"))