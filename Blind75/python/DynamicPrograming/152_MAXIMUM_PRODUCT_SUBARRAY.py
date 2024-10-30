# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        currentMax = currentMin = tempMax = result = nums[0]


        for i in range(1,len(nums)):
            tempMax = max(nums[i] , currentMax * nums[i] , currentMin*nums[i])
            currentMin = min(nums[i] , currentMax * nums[i] , currentMin*nums[i])
            currentMax = tempMax

            result = max(result , currentMax)
        return result




sol = Solution()
print(sol.maxProduct( nums = [2,3,-2,4]))
