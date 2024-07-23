# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]




from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] = 1 + hash[num]
            else:
                hash[num] = 1
            # print(hash)
        
        result = []
        for _ in range(k):
            max_freq = -1
            max_freq_num = None
            # loop through items and compair freq to current max_freq
            # highets will be removed and loop again with remainder to find k values
            for num, freq in hash.items():
                print (num , freq)
                if freq > max_freq:
                    max_freq = freq
                    max_freq_num = num
            result.append(max_freq_num)
            # Remove the found max element to find the next one
            hash.pop(max_freq_num)

        return result 
sol = Solution()
ans = sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
print(ans)