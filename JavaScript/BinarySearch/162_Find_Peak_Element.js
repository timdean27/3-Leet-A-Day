// A peak element is an element that is strictly greater than its neighbors.

// Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

// You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

// You must write an algorithm that runs in O(log n) time.

// Input: nums = [1,2,3,1]
// Output: 2
// Explanation: 3 is a peak element and your function should return the index number 2.

var findPeakElement = function(nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        let mid = Math.floor((left + right) / 2);
        if (nums[mid] < nums[mid + 1]) {
            // Peak is on the right side
            left = mid + 1;
        } else {
            // Peak is on the left side or mid is the peak
            right = mid;
        }
    }

    // At the end of the loop, left and right will be equal and pointing to a peak
    return left;
}

console.log(findPeakElement([1,2,3,1]))
console.log(findPeakElement([1,2,1,3,5,6,4]))


// Comparing every element: 
// If you iterate through the array using a 
// for loop and compare each element with its neighbors, 
// you would need to check every element to determine 
// if it's a peak or not. 
// This would take linear time, 
// resulting in O(n) time complexity.

// Requirement for O(log n) 
// time complexity: 
// The problem specifies that the algorithm should 
// run in O(log n) time. To achieve this, 
// you need an approach that reduces the search space 
// in each step, such as binary search.