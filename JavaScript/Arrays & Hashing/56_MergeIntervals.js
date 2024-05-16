// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

// Example 1:

// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].



var merge = function(intervals) {
    if (intervals.length <= 1) return intervals; 
    intervals.sort((a, b) => a[0] - b[0]);
    let currentStart = intervals[0][0];
    let currentEnd = intervals[0][1];
    const result =[]
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] <= currentEnd) {
            // If the current interval overlaps with the previous one, update the currentEnd
            currentEnd = Math.max(currentEnd, intervals[i][1]);
        } else {
            // If there's no overlap, push the previous merged interval to the result and update currentStart and currentEnd
            result.push([currentStart, currentEnd]);
            currentStart = intervals[i][0];
            currentEnd = intervals[i][1];
        }
    }
    
    // Push the last merged interval to the result
    result.push([currentStart, currentEnd]);
    
    return result;
};

console.log(merge([[1,3],[2,6],[8,10],[15,18]]))