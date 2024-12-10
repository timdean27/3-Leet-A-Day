class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        answer = False
        for num in nums:
            if num in hash:
                answer = True
            else:
                hash[num] = num
        return answer

        
sol = Solution()
print(sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
