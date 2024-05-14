// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

 

// const twoSum =(nums , target) =>{

//     let x = 0
//     while (x < nums.length-1){
//     for(let i = x+1; i < nums.length; i++){  
//         let sum = nums[x] + nums[i]
//         console.log(sum)
//         if(sum == target){
//             return [x,i]
//         }
//     }
//     x++
// }

// }

// console.log(twoSum([2,5,5,11], 10))

// const twoSum = (nums, target) => {
//     const hash = {};
//     for (let i = 0; i < nums.length; i++) {
//         let potentialKey = target - nums[i];
//         if (hash[potentialKey] !== undefined) {
//             return [i, hash[potentialKey]];
//         } else {
//             hash[nums[i]] = i;
//         }
//     }
// };

// console.log(twoSum([2, 7, 11, 15], 9)); // Output: [1, 0] (because nums[1] + nums[0] = 7 + 2 = 9)


const twoSum =(nums , target) =>{

    const hash = {}
    //set hash key to value of index and value to index 
    //ex: nums[1] = 7 hash would be hash[7] = 1
    for(let i = 0 ; i < nums.length; i++){
        let val = nums[i]
        hash[val] = i
        console.log(hash)
    }
    //get target - current nums[i]
    // if value is in hash then nums[i] + hash[value] = target
    // return current index and index stored in hash
    for(let i = 0 ; i < nums.length; i++){
        let potentailKey = target - nums[i]
        if(hash[potentailKey] && hash[potentailKey] !== i){
            return [i, hash[potentailKey]]
        }
    }

}

console.log(twoSum([2,7,11,15], 9))


