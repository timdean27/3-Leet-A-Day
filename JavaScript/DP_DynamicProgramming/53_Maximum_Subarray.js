// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// A subarray is a contiguous part of an array.

 

// Example 1:

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.
// Example 2:

// Input: nums = [1]
// Output: 1
// Example 3:

// Input: nums = [5,4,-1,7,8]
// Output: 23


const maxSubArray = (nums)=>{
    if(nums.length == 1) return nums[0];
    let currentMax = nums[0]
    let maxValue = nums[0]
    for(let i=1; i<nums.length; i++){
        currentMax = Math.max(nums[i] , nums[i]+currentMax)
        maxValue = Math.max(maxValue,currentMax)
    }
    return maxValue
}


console.log(maxSubArray([5,4,-1,7,8]))