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
        nums.sort()  # Sort the list to handle duplicates easily
        answer = []
        
        for i in range(len(nums)):
            # To avoid duplicates, skip the same value
            if i > 0 and nums[i] == nums[i - 1]:
                continue # continue means skip to next value of loop 
            
            left = i +1
            right = len(nums) -1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    # only shift left pointer the loop will handle the situation where right is too larger 
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left +=1
        return answer
sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))
# Output: [[-1,-1,2],[-1,0,1]]


