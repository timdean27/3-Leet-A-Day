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
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 


def TwoSum(nums, target):
    # Create an empty dictionary to store seen values along with their indices
    seen = {}  
    
    # Loop through the array along with their indices
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement is already seen
        if complement in seen:
            # If yes, return the indices of the two numbers that add up to the target
            return [seen[complement], i]  
        
        # Store the current number along with its index in the dictionary
        seen[num] = i  
    
    # If no solution is found, return None
    return None  
