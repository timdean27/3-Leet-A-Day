# Given an integer array nums, return true if any 
# value appears at least twice in the array, 
# and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

from typing import List

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
        # range(len(nums)) generates a sequence of indices from 0 to the length of the list minus one.
            for j in range(i + 1, len(nums)):
            # It iterates over each index j starting from i + 1 to the end of the list.
            # This ensures that each element nums[i] is compared only with the elements that come after it in the list.
                if nums[i] == nums[j]:
                    return True
        return False
    
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Create an instance of the Solution class
sol1 = Solution1()
sol2 = Solution2()

# Call the method using the instance
ans1 = sol1.containsDuplicate([1, 2, 3, 1])
ans2 = sol2.containsDuplicate([1, 2, 3, 1])

print(ans1)  
print(ans2)  