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




class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = len(nums) - 1
        left = 0
        # If the array is already sorted and not rotated, return the first element.
        if nums[left] < nums[right]:
            return nums[left]
        # find the piviot where left is no longer increaseing and right is no longer decresing 
        while right > left + 1:
            # print(nums[left], nums[right] )
            if nums[left] > nums[left + 1]:
                # if value of left+1 is less then the current left it means we stoped increase and hit the lowest value
                return nums[left + 1]
            if nums[right] < nums[right - 1]:
                # if value of right-1 is greater then the current right it means we stoped decreaseing and hit the lowest value
                return nums[right]
            else:
                left +=1
                right -=1
            # when we it the piviot point exit the while loop and return the min of the two final values
        return min(nums[left] , nums[right])


sol = Solution()
print(sol.findMin(nums = [3,4,5,1,2]))
# print(sol.findMin(nums = [4,5,6,7,0,1,2]))
# print(sol.findMin(nums = [11,13,15,17]))