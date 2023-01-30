// Given an integer array nums, find a 
// subarray
//  that has the largest product, and return the product.

// The test cases are generated so that the answer will fit in a 32-bit integer.

 

// Example 1:

// Input: nums = [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.
// Example 2:

// Input: nums = [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


var maxProduct = function(nums) {
    
    //max produc sub array means -2*-3 = 6
    // because of negatives we want to store the previous max and previous min
    let previousMax = nums[0];
    let previousMin = nums[0];
    let Max = nums[0]
    for(let i = 1; i < nums.length; i++) {
            let currentMax = Math.max(nums[i], previousMax*nums[i], previousMin*nums[i]);
            console.log("find current max",currentMax)
            let currentMin = Math.min(nums[i], previousMax*nums[i], previousMin*nums[i]);
            console.log("find current min",currentMin)
            previousMax = currentMax
            previousMin = currentMin

            Max = Math.max(currentMax, Max)
            console.log("find new Max",Max)
    }
    return Max
};

console.log(maxProduct([2,3,-2,4]))