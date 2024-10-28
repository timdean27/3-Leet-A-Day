# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.


 
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            twoPrior = i -2
            prior = i -1
            # check if it is better to use the prior sotred value or if is better to add current value to two prior
            #  if the new value does not increase you above the house you have orbbed so far then skip it
            dp[i] = max(dp[prior] , nums[i]+ dp[twoPrior])

        # The last element in dp represents the maximum money we can rob
        return dp[-1]



sol = Solution
print(sol.rob(nums = [2, 7, 9, 3, 1]))

# explained 

# dp[0] = nums[0] = 2
# dp[1] = max(nums[0], nums[1]) = max(2, 7) = 7
# dp[2] = max(dp[1], nums[2] + dp[0]) = max(7, 9 + 2) = max(7, 11) = 11
# dp[3] = max(dp[2], nums[3] + dp[1]) = max(11, 3 + 7) = max(11, 10) = 11  , skip house 3 , keeping what we have so far
# dp[4] = max(dp[3], nums[4] + dp[2]) = max(11, 1 + 11) = max(11, 12) = 12




from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        rob1 , rob2 = 0 , 0
        for i in range(len(nums)):
            newRob = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = newRob
        
        return rob2


sol = Solution
print(sol.rob(nums = [2, 7, 9, 3, 1]))