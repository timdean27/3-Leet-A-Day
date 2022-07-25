// Given a 0-indexed integer array nums of length n and an integer k, 
//return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
 

// Example 1:

// Input: nums = [3,1,2,2,2,1,3], k = 2
// Output: 4
// Explanation:
// There are 4 pairs that meet all the requirements:
// - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
// - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
// - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
// - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
// Example 2:

// Input: nums = [1,2,3,4], k = 1
// Output: 0
// Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.


var countPairs = function(nums, k) {
    let result = 0;
    for(let i = 0; i < nums.length; i++){
        for(let j = i+1; j < nums.length; j++){
                // console.log(nums[i],i,nums[j],j)
                if(nums[i] == nums[j]){
                    // console.log(nums[i],i,nums[j],j)
                    // console.log(i*j)
                    if((i*j)%k ==0){
                        // console.log("i*j",i*j)
                        result++
                    }

                }
        }
    }
    return result;
};

// console.log(countPairs([3,1,2,2,2,1,3],2))
// console.log(countPairs([1,2,3,4],1))
console.log(countPairs([5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3],7))


// 
/*
answer took 14 mins 
Runtime: 109 ms, faster than 29.82% of JavaScript online submissions for Count Equal and Divisible Pairs in an Array.
Memory Usage: 43.1 MB, less than 17.17% of JavaScript online submissions for Count Equal and Divisible Pairs in an Array.


*/