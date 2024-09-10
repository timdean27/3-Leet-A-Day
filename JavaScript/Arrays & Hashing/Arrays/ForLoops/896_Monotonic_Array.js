// An array is monotonic if it is either monotone increasing or monotone decreasing.

// An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

// Given an integer array nums, return true if the given array is monotonic, or false otherwise.
// Example 1:

// Input: nums = [1,2,2,3]
// Output: true


var isMonotonic = function(nums) {
    let increasing = true
    let decreasing = true
    let latest = nums[0]
    for(let i = 1 ; i < nums.length; i++){
        if (latest == nums[i]) continue
        if(latest < nums[i]){
            decreasing = false
        }
        if(latest > nums[i]){
            increasing = false
        }
        latest = nums[i]
    }
    if(increasing || decreasing) return true 
    else return false
};

console.log(isMonotonic([1,2,2,3]))
console.log(isMonotonic([6,5,4,4]))
console.log(isMonotonic([1,3,2]))