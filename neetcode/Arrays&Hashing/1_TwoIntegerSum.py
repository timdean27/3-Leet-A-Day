# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

class Solution:
    def twoIntegerSum(self , nums , target):
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if(nums[i]+nums[j] == target):
                    return [i,j]
        return False




sol = Solution()
answer = sol.twoIntegerSum
print(answer(nums = [3,4,5,6], target = 7))
    