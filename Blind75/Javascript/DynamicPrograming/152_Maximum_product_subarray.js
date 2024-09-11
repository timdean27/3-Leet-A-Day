// # Given an integer array nums, find a 
// # subarray
// #  that has the largest product, and return the product.

// # The test cases are generated so that the answer will fit in a 32-bit integer.

 

// # Example 1:

// # Input: nums = [2,3,-2,4]
// # Output: 6
// # Explanation: [2,3] has the largest product 6.
// # Example 2:

// # Input: nums = [-2,0,-1]
// # Output: 0
// # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


// # Rember we are not finding the largest product of 2 variables we are finding the largest consecutive substring 
// # example [2,3,-2,4] we get [2,3] = 6 , if we did [2,3,-2] we get -12 but we can not get back to positive becasue next value is 4, if the list kept going maybe we could 
// from typing import List

var maxProduct = function(nums) {

    let currentMax =nums[0]
    let currentMin = nums[0]
    let tempMax =nums[0]
    let tempMin = nums[0]
    let result = nums[0]

    for(let i = 1 ; i < nums.length ; i++){
        let tempMax = Math.max(nums[i], nums[i] *currentMax ,  nums[i] *currentMin)
        let tempMin = Math.min(nums[i], nums[i] *currentMax ,  nums[i] *currentMin)
        currentMax = tempMax
        currentMin = tempMin
        result = Math.max(result , currentMax)

    }
    return result

}


console.log(maxProduct([2,3,-2,4]))