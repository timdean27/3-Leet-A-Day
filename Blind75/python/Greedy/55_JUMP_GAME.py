# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        furthest_we_can_jump = 0
 
        for i in range(len(nums)):
            if i > furthest_we_can_jump:
                return False

            # furthest_we_can_jump starts at 0 so first we updates to 0 + nums[0] 
            # then we have furthest_we_can_jump = 2 , we check 1 + nums[1] is greater than 2 we now make this the fursthest we can go
            #  if at some point furthest_we_can_jump remains the largest and its less than len(nums) we cant jump out
            furthest_we_can_jump = max(furthest_we_can_jump , i + nums[i])
            print(furthest_we_can_jump)
            
            if furthest_we_can_jump >= len(nums) - 1:
                return True


sol = Solution()
print(sol.canJump(nums = [2,3,1,1,4]))