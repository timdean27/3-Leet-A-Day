# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        currentSum = nums[0]
        maxSum = nums[0]
        temp_start = 0
        start = 0
        end = 0
        
        for i in range(1, len(nums)):
            if currentSum + nums[i] < nums[i]:
                currentSum = nums[i]
                temp_start = i
            else:
                currentSum += nums[i]
            
            if currentSum > maxSum:
                maxSum = currentSum
                start = temp_start
                end = i

        finalSub = nums[start:end+1]
        
        return maxSum

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))