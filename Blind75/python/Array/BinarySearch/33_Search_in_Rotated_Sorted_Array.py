# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = (right + left) // 2  # Use integer division to avoid floating-point issues
            # If the target is found, return its index
            if nums[mid] == target:
                return mid
            # check if the left side is sorted smallest to largest with mid being largest 
            elif(nums[left] <= nums[mid]):
                # now that left is sorted check where target lies and adjust 
                if(nums[left]<= target < nums[mid]):
                    # target is in between left and current mid so we can set right to mid -1
                    right = mid -1 
                else:
                    # target is not found on left side of mid so we change left to mid+1
                    left = mid +1
            # Otherwise, the right half is sorted
            else:
                # if right is sorted check where target lies inbetween mid and right
                if(nums[mid]< target <= nums[right]):
                # target is in between mid and current right so we can set left to mid +1
                    left = mid + 1
                else:
                    right = mid - 1
        # If the target is not found, return -1
        return -1

sol = Solution()
print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))