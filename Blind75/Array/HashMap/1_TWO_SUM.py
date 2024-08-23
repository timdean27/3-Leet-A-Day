# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            # if the diffrince from the target - nums[i] already in the hash then return index of that value and current i 
            diffrence = target - nums[i]
            if diffrence in hash:
                return[hash[diffrence] , i]
            # if not then push the value of nums[i] into the hash to test vs future diffrences
            hash[nums[i]] = i

sol = Solution()

print(sol.twoSum(nums = [2,7,11,15], target = 9))
print(sol.twoSum(nums = [3,2,4], target = 6))
print(sol.twoSum(nums = [3,3], target = 6))