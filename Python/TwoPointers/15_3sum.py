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


class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        if len(nums) < 3:
            return result
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lowPointer = i + 1
            highPointer = len(nums) - 1

            while lowPointer < highPointer:
                total = nums[i] + nums[lowPointer] + nums[highPointer]

                if total < 0:
                    lowPointer += 1
                elif total > 0:
                    highPointer -= 1
                else:
                    result.append([nums[i], nums[lowPointer], nums[highPointer]])

                    # Skip duplicates to avoid duplicate triplets
                    while lowPointer < highPointer and nums[lowPointer] == nums[lowPointer + 1]:
                        lowPointer += 1
                    while lowPointer < highPointer and nums[highPointer] == nums[highPointer - 1]:
                        highPointer -= 1

                    lowPointer += 1
                    highPointer -= 1

        return result

# Test case
instance = Solution()
print(instance.threeSum([-1, 0, 1, 2, -1, -4]))
print(instance.threeSum([1, -1, -1, 0]))
print(instance.threeSum([0,0,0,0]))
