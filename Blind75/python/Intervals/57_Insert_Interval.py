# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        checkedIntervals = []
        for i in range(len(intervals)):
            # if last of newinterval list is less then start of next interval stick new interval in checked and add the remainng 
            if newInterval[-1] < intervals[i][0]:
                checkedIntervals.append(newInterval)
                # once newInterval is in checkedIntervals append all others 
                return checkedIntervals + intervals[i:]
            
            # if newInterval starts at a larger value than append the smaller intervals 
            elif newInterval[0] > intervals[i][1]:
                checkedIntervals.append(intervals[i])
            
            # else if new interval has shared values use  the smallest start and the largest end to merdge the two 
            else:
                newInterval = [min(newInterval[0], intervals[i][0]) , max(newInterval[-1] , intervals[i][-1])]

        # If we reach the end without inserting the new interval, add it
        checkedIntervals.append(newInterval)
        return checkedIntervals
sol = Solution()
print(sol.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))