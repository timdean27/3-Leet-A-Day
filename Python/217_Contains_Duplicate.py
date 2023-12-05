# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

# Call the function directly
result = containsDuplicate([1, 2, 3, 1])

# Print the result
print(result)


# from typing import List

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False

# # Create an instance of the Solution class
# sol = Solution()

# # Call the containsDuplicate method on the instance
# result = sol.containsDuplicate([1, 2, 3, 1])

# # Print the result
# print(result)
