# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        
        longest_streak = 1
        current_streak = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    longest_streak += 1

                else:
                    longest_streak = 1
            current_streak = max(current_streak,longest_streak)
        return current_streak
    
sol = Solution()
print(sol.longestConsecutive(nums = [100,4,200,1,3,2]))