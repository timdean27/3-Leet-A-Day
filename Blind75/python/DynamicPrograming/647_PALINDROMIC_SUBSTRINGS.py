# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0


        def checkPalindrom(left , right, count):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
                count += 1
            return  count
        
        for i in range(len(s)):
            left = right = i
            # for odd palindrom
            count = checkPalindrom(left,right, count)
            # for even palindrom
            count = checkPalindrom(left , right +1, count)

        return count
    
sol = Solution()
print(sol.countSubstrings(s = "abc"))