// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:

// Input: nums = [1,2,3,1]
// Output: true
// Example 2:

// Input: nums = [1,2,3,4]
// Output: false
// Example 3:

// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true


var containsDuplicate = function(nums) {
    nums.sort((a,b)=> a - b)
    console.log(nums)
    let result = 0
    for(let i = 0; i < nums.length; i++){
        console.log(nums[i+1])
        console.log(nums[i])
        if(nums[i] == nums[i+1]){
            result = 1
        }
    }
    if(result > 0){
        return true
    }
    else{return false}
};

// console.log(containsDuplicate([1,2,3,1]))
// console.log(containsDuplicate([1,2,3,4]))
// console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
console.log(containsDuplicate([2,14,18,22,22]))