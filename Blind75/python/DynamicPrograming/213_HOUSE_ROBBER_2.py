# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3


 
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Handle edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        def helpfun(nums: List[int]) -> int:
            rob1, rob2 = 0, 0
            
            for i in range(len(nums)):
                newRob = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2

        # Calculate the maximum money by considering two scenarios:
        # Scenario 1: Exclude the last house
        # Scenario 2: Exclude the first house
        return max(helpfun(nums[:-1]), helpfun(nums[1:]))

sol = Solution
print(sol.rob([2,3,2]))