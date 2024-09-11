// Given an integer array nums, find the 
// subarray
//  with the largest sum, and return its sum.

// Example 1:
// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: The subarray [4,-1,2,1] has the largest sum 6.
// Example 2:

// Input: nums = [1]
// Output: 1
// Explanation: The subarray [1] has the largest sum 1.
// Example 3:

// Input: nums = [5,4,-1,7,8]
// Output: 23
// Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


var maxSubArray = function(nums) {

// we will check the addition of the ellemnt to the current sum
// if the addition of the element remains less than the element we reset at this element 
// exapmple [-2 ,1] aditon of 1 to -2 = -1 which is less than 1
// we set the start to i , since this is the new start of our subarray

//  if current sum plus the new number is graeter than current sum 
let currentSum = nums[0]
let maxSum = nums[0]
let start = 0 
let end = 0
let tempStart = 0;
    for(let i = 1 ; i < nums.length ; i++){

        if(currentSum + nums[i] < nums[i]){
            currentSum = nums[i]
            tempStart = i
        }

        else currentSum += nums[i]

        if( currentSum > maxSum){
            maxSum = currentSum
            start = tempStart;
            end = i
        }

    }
    let subArray = nums.slice(start, end + 1)
    console.log(subArray)
    return maxSum;
    
};

console.log(maxSubArray(nums =
    [-2,1,-3,4,-1,2,1,-5,4]))