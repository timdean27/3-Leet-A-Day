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


# Rember we are not finding the largest product of 2 variables we are finding the largest consecutive substring 
# example [2,3,-2,4] we get [2,3] = 6 , if we did [2,3,-2] we get -12 but we can not get back to positive becasue next value is 4, if the list kept going maybe we could 
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # set the current max to nums
        currentMax = currentMin = tempMax = result = nums[0]

        for i in range(len(nums)):
            # check for nex max in temp max , between current nums[i] , and if this new number increases product by mutiplying to current max or current min
            tempMax = max(nums[i], currentMax*nums[i] , currentMin*nums[i])
            # store current min , incase next number is negative which will create a new max
            currentMin = min(nums[i] , currentMax*nums[i] , currentMin*nums[i])
            # save tempmax to current max
            currentMax = tempMax

            # check if max is a previous max or the current max
            result = max(result, currentMax)
        return result

sol = Solution()

print(sol.maxProduct([2,3,-2,4]))  # Output: 6   Explanation: [2,3] has the largest product 6.




class Solution(object):
    def maxProduct(self, nums):

        if not nums:
            return 0
        
        currentMax = nums[0]
        currentMin = nums[0]
        result= nums[0]

        # Iterate through the array
        for i in range(1, len(nums)):
            # Store the current values of max
            holdValue = currentMax
            if nums[i] < 0:
                # Swap currentMax and currentMin when current is negative say current number is -4 and currentMin is -6 we want to set our current max to 24
                currentMax = currentMin
                currentMin = holdValue

            # Update currentMax and currentMin
            currentMax = max(nums[i], currentMax * nums[i])
            currentMin = min(nums[i], currentMin * nums[i])
            
            # Update result
            result = max(result, currentMax)

        return result

# sol = Solution()
# print(sol.maxProduct([-2]))  # Output: -2
# print(sol.maxProduct([0, 2]))  # Output: 2
# print(sol.maxProduct([-2, 3, -4]))  # Output: 24   

# for array [-2, 3, -4]
# set currentMax = currentMin = result= nums[0]
# Step 1: Process 3

# Current element: 3

# Check for Negative: 3 is positive, so no swapping of currentMax and currentMin.

# Update currentMax:

# currentMax = max(3, -2 * 3)
# Calculation: max(3, -6) = 3
# New currentMax: 3
# Update currentMin:

# currentMin = min(3, -2 * 3)
# Calculation: min(3, -6) = -6
# New currentMin: -6
# Update result:

# result = max(-2, 3)
# New result: 3
# Step 2: Process -4
# Current element: -4

# Check for Negative: -4 is negative, so swap currentMax and currentMin:

# Before Swap: currentMax = 3, currentMin = -6
# After Swap: currentMax = -6, currentMin = 3
# Update currentMax:

# currentMax = max(-4, -6 * -4)
# Calculation: max(-4, 24) = 24
# New currentMax: 24
# Update currentMin:

# currentMin = min(-4, 3 * -4)
# Calculation: min(-4, -12) = -12
# New currentMin: -12
# Update result:

# result = max(3, 24)
# New result: 24
