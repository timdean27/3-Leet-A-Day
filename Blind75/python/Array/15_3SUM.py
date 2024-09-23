# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the nums array 
        nums.sort()
        result = []
        
        # Step 2: Iterate through the array until the second-to-last element
        # we can use len(nums -2) becasue we know right will start at len(nums) -1
        for i in range(len(nums) - 2):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # set pointers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sumNums = nums[i] + nums[left] + nums[right]
                # if sum of numbers is less than zero we shift the left up increaseing value (left is lowest)
                if sumNums < 0:
                    left += 1
                # if sum of numbers is greater than zero we shift the right down decreasing value (right is largest)
                elif sumNums > 0:
                    right -= 1
                # if sum of 3 numbers is zero push array triple to result
                elif sumNums == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # increment the left value
                    left +=1
                    # check if the new left value is a duplicite of the last left value if it is increment again
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
      
        
        return result




sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))