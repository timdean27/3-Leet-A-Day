// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

 

// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation: 
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.


var threeSum = function(nums) {
    nums.sort((a, b) => a - b);
    const result = []
    for(let i = 0 ; i < nums.length  -2; i++){
        // continue is use to skip the itteration
        //that is if nums[i] is same as last it will skip 
        //and go to next vlue of i
        if(i > 0 && nums[i] === nums[i-1]) continue;
        let left = i + 1;
        let right = nums.length - 1;
        
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);
                
                // Avoid duplicates but makeing sure current left 
                //and current right are not repeated
                // the values will increment or decrement while they remiain repeated
                while (left < right && nums[left] === nums[left + 1]) 
                    {left++}
                while (left < right && nums[right] === nums[right - 1]) 
                    {right--}
                
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    
}

return result;
}

console.log(threeSum([-1,0,1,2,-1,-4]))