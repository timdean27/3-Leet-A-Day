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
        hashMap = {}
        left = right = topFrequency = longest= 0 

        while(right < len(s)):

            # This attempts to retrieve the value for the key s[right] from the dictionary hashMap.
            # If the key exists in hashMap, it returns the corresponding value.
            # If the key does not exist, it returns the default value 0.
            # Whether the value is retrieved (an existing count) or 0 (for a new character), it adds 1 to that value.
            hashMap[s[right]] = hashMap.get(s[right], 0) + 1

            # Update the topFrequency (most frequent character in the current window)
            topFrequency = max(topFrequency , hashMap[s[right]])

            # If the current window (right - left + 1) is invalid (i.e., too many characters to replace)
            if (right - left + 1) - topFrequency > k:
                # Shrink the window by moving the left pointer
                hashMap[s[left]] -= 1
                left += 1

            # Update the longest valid substring found so far
            longest = max(longest, right - left + 1)
            # Move the right pointer to expand the window
            right += 1
        return longest


sol = Solution()
print(sol.characterReplacement(s = "ABAB", k = 2))