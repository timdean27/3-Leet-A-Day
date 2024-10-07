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

        # helper function to check for palandrom
        def isPalindrome(left,right , count):
            # check that left and right are inbounds and that left and right are equal if not then its not palindrom and dont need to continue
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        for i in range(len(s)):
            # starting from single character "cabac"
            count = isPalindrome(i, i , count)
            # starting from a pair of characteres example "cabbac"
            count = isPalindrome(i, i + 1 , count)

        return count



sol = Solution()
print(sol.countSubstrings(s = "abc"))