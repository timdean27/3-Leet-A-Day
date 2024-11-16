# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

 

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.


class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of digits (as characters)
        num_list = list(str(num))
        # we will want to swap the largest value with the value of most significance 
        left = 0
        while left < len(num_list):
            largest = num_list[left]
            indexLargest = left
            for i in range(left+1,len(num_list)):
                if num_list[i] >= largest:
                    largest = num_list[i]
                    indexLargest = i
            # Swap if we found a larger digit further in the list
            if left != indexLargest and largest != num_list[left]:
                num_list[left], num_list[indexLargest] = num_list[indexLargest], num_list[left]
                break  #once swap is complete we break we only need one swap
            left += 1
        return int("".join(num_list))



sol = Solution()
print(sol.maximumSwap(1993)) 