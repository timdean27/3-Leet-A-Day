// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]

var topKFrequent = function(nums, k) {
    let mainHash = {};
    for (let i = 0; i < nums.length; i++) {
        if (mainHash[nums[i]]) {
            mainHash[nums[i]]++;
        } else {
            mainHash[nums[i]] = 1;
        }
    }
    console.log(mainHash)
    console.log(Object(mainHash));
    console.log(Object.keys(mainHash));
  
    let uniqueNums = Object.keys(mainHash);
    console.log(uniqueNums)
    // Sort the unique numbers by their frequencies in descending order
    uniqueNums.sort((a, b) => mainHash[b] - mainHash[a]);
    console.log(uniqueNums)
    // Get the top k frequent elements
    let result = [];
    for (let i = 0; i < k; i++) {
        result.push(parseInt(uniqueNums[i]));
    }

    return result;
};

console.log(topKFrequent([1,1,1,2,2,2,2,2,3,3], 2))