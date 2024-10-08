# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for letters in s:
            if letters.isalpha() or letters.isdigit():
                new += letters.lower()

        backward = ''
        for i in range(1, len(new) + 1):
            backward += new[len(new) - i]


        return backward == new

# Create an instance of the Solution class
sol = Solution()

# Call the isPalindrome method
result = sol.isPalindrome("A man, a plan, a canal: Panama")
print(result)
