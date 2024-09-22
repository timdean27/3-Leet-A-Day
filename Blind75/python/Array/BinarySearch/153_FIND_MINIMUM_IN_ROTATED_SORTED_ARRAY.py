# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 



# for this problem it does not matter the rotations much
# we are just doing binary search
# left mid and right
# if mid is higher than the right then we know that the min must be between right adn mid , so we set left to mid+1 and restart
# If nums[mid] <= nums[right]:This suggests that the minimum is either at mid or in the left half (including mid itself) because the right half is already sorted (if nums[mid] <= nums[right]).
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while(left < right):
            mid = (right + left) // 2  # Use integer division to avoid floating-point issues
            if(nums[right]< nums[mid]):
                left = mid+1
            else:
                right = mid

        return nums[left]
        


sol = Solution()
print(sol.findMin(nums = [3,4,5,1,2]))
# print(sol.findMin(nums = [4,5,6,7,0,1,2]))
# print(sol.findMin(nums = [11,13,15,17]))