// Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

// If target is not found in the array, return [-1, -1].

// You must write an algorithm with O(log n) runtime complexity.

// Example 1:

// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]
// Example 2:

// Input: nums = [5,7,7,8,8,10], target = 6
// Output: [-1,-1]
// Example 3:

// Input: nums = [], target = 0
// Output: [-1,-1]

var searchRange = function (nums, target) {
  let result = [-1, -1];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === target && nums[i - 1] != target) {
      result = [i, i];
    }
    if (nums[i] === target && nums[i - 1] === target) {
      result.splice(1, 1, i);
    }
  }
  return result;
};

console.log(searchRange([5, 7, 7, 8, 8, 10], 8));
console.log(searchRange([5, 7, 7, 8, 8, 10], 6));
console.log(searchRange([6], 6));
