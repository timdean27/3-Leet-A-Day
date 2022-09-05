// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]


var topKFrequent = function(nums, k) {
    nums.sort((a,b)=> a - b)
    let hash = {}
    let result = []
    for(let i = 0; i < nums.length; i++){
        //if hash already exists push nums[i] into key
        if(hash[nums[i]]){
            hash[nums[i]]++
        }
        //else if hash does not exist set hash name with nums[i] = to nums[i]
        else{
            hash[nums[i]] = 1
        }
    }
    let values = Object.values(hash)
    console.log("values",values)
    let sorted = values.sort((a,b)=> b-a)
    console.log("sorted",sorted)

    let k_Values = sorted.slice(0, k)
    console.log("k_Values",k_Values)
    let keys = Object.keys(hash)
    console.log("keys ", keys )
    console.log(hash)

    //need to unsort values
    values = Object.values(hash)
    console.log("values",values)

    for(let i = 0; i < values.length; i++){
        for(let j = 0 ; j <= k; j++){
            // console.log("values[i]" ,values[i] , i)
            if(values[i] == k_Values[j] && k_Values[j] != k_Values[j-1]){
                result.push(keys[i])
            }
        }
    }
    return result
};

// console.log(topKFrequent([1,1,2,2,2,3,4,4,4,4,4],2))
// console.log(topKFrequent([1,2],2))
console.log(topKFrequent([4,1,-1,2,-1,2,3] ,2))