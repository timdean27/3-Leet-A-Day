# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the dp array where dp[i] represents the length of the longest increasing subsequence ending at index i
        dp = [1] * len(nums)
        # each number starts at 1 , meanign only its self to begin is in sequince 




        for i in range(1,len(nums)):
            # print("i", i)

            for j in range(0,i):
                print("i and j", i , j)
                print("nums[i] , nums[j]", nums[i], nums[j])
        # we will loop through an compair each new number vs the previous numbers before it 
        # if the current number is greateer than the number before it then we add +1 do the dp[i]
        # the max dp value at the end is the value for the largest sequince
                if nums[i] < nums[j]:
                    # print("dp[i] , dp[j]", dp[i], dp[j])
                    dp[i] = max(dp[i], dp[j] + 1)
                    print(dp)


        return max(dp)
        


sol = Solution()
print(sol.lengthOfLIS(nums = [0, 1, 0, 3, 2, 3]))

# First Loop (i = 1):
# j = 0:
# Compare nums[1] (1) with nums[0] (0).
# Since nums[1] > nums[0], update dp[1]:
# dp[1] = max(dp[1], dp[0] + 1) = max(1, 1 + 1) = 2
# Updated dp: [1, 2, 1, 1, 1, 1]

# Second Loop (i = 2):
# j = 0:
# Compare nums[2] (0) with nums[0] (0).
# Since nums[2] < nums[0], dp[2] remains the same.
# dp: [1, 2, 1, 1, 1, 1]

# j = 1:
# Compare nums[2] (0) with nums[1] (1).
# Since nums[2] < nums[1], dp[2] remains the same.
# dp: [1, 2, 1, 1, 1, 1]

# Third Loop (i = 3):
# j = 0:
# Compare nums[3] (3) with nums[0] (0).
# Since nums[3] > nums[0], update dp[3]:
# dp[3] = max(dp[3], dp[0] + 1) = max(1, 1 + 1) = 2
# Updated dp: [1, 2, 1, 2, 1, 1]

# j = 1:
# Compare nums[3] (3) with nums[1] (1).
# Since nums[3] > nums[1], update dp[3]:
# dp[3] = max(dp[3], dp[1] + 1) = max(2, 2 + 1) = 3
# Updated dp: [1, 2, 1, 3, 1, 1]

# j = 2:
# Compare nums[3] (3) with nums[2] (0).
# Since nums[3] > nums[2], dp[3] could be updated but dp[3] is already 3, so it remains 3.
# dp: [1, 2, 1, 3, 1, 1]

# Fourth Loop (i = 4):
# j = 0:
# Compare nums[4] (2) with nums[0] (0).
# Since nums[4] > nums[0], update dp[4]:
# dp[4] = max(dp[4], dp[0] + 1) = max(1, 1 + 1) = 2
# Updated dp: [1, 2, 1, 3, 2, 1]

# j = 1:
# Compare nums[4] (2) with nums[1] (1).
# Since nums[4] > nums[1], update dp[4]:
# dp[4] = max(dp[4], dp[1] + 1) = max(2, 2 + 1) = 3
# Updated dp: [1, 2, 1, 3, 3, 1]

# j = 2:
# Compare nums[4] (2) with nums[2] (0).
# Since nums[4] > nums[2], dp[4] remains 3 because it's already at the maximum value.
# dp: [1, 2, 1, 3, 3, 1]

# j = 3:
# Compare nums[4] (2) with nums[3] (3).
# Since nums[4] < nums[3], dp[4] remains the same.
# dp: [1, 2, 1, 3, 3, 1]

# Fifth Loop (i = 5):
# j = 0:
# Compare nums[5] (3) with nums[0] (0).
# Since nums[5] > nums[0], update dp[5]:
# dp[5] = max(dp[5], dp[0] + 1) = max(1, 1 + 1) = 2
# Updated dp: [1, 2, 1, 3, 3, 2]

# j = 1:
# Compare nums[5] (3) with nums[1] (1).
# Since nums[5] > nums[1], update dp[5]:
# dp[5] = max(dp[5], dp[1] + 1) = max(2, 2 + 1) = 3
# Updated dp: [1, 2, 1, 3, 3, 3]

# j = 2:
# Compare nums[5] (3) with nums[2] (0).
# Since nums[5] > nums[2], dp[5] remains 3 because it's already at the maximum value.
# dp: [1, 2, 1, 3, 3, 3]

# j = 3:
# Compare nums[5] (3) with nums[3] (3).
# Since nums[5] == nums[3], dp[5] remains the same.
# dp: [1, 2, 1, 3, 3, 3]

# j = 4:
# Compare nums[5] (3) with nums[4] (2).
# Since nums[5] > nums[4], update dp[5]:
# dp[5] = max(dp[5], dp[4] + 1) = max(3, 3 + 1) = 4
# Updated dp: [1, 2, 1, 3, 3, 4]