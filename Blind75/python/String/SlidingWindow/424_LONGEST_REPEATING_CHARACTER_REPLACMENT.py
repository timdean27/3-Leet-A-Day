# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countChars = {}
        left = longest= 0 

        for right in range(len(s)):
            # map the frequincey of characters in s
            countChars[s[right]] = 1 + countChars.get(s[right],0)
            windowLen = (right - left)+ 1
            # check that the characters in the current window are 
            # all the max character excepet the acceptable amount of values we can replace k
            while (windowLen - max(countChars.values()) > k):
                countChars[s[left]] -= 1
                left +=1
                windowLen = (right - left)+ 1

            longest = max(longest , windowLen)

        return longest
        

sol = Solution()
print(sol.characterReplacement(s = "ABAB", k = 2))