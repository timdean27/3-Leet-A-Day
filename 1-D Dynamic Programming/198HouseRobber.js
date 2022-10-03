// You are a professional robber planning to rob houses along a street. 
// Each house has a certain amount of money stashed, the only constraint stopping you from 
// robbing each of them is that adjacent houses have security systems connected and it will 
// automatically contact the police if two adjacent houses were broken into on the same night.

// Given an integer array nums representing the amount of money of each house, 
// return the maximum amount of money you can rob tonight without alerting the police.

 

// Example 1:

// Input: nums = [1,2,3,1]
// Output: 4
// Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
// Total amount you can rob = 1 + 3 = 4.
// Example 2:

// Input: nums = [2,7,9,3,1]
// Output: 12
// Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
// Total amount you can rob = 2 + 9 + 1 = 12.



let rob =(nums) =>{
    if(!nums.length) return 0
    if(nums.length === 1) return nums[0]
    if(nums.length === 2) return Math.max(nums[0], nums[1])

    for(let i = 2; i < nums.length; i++) {
        // we will start at i = 2 and nums = [2,1,2,1,5,2,1]
        // we will check the larger of  nums[i-2]+nums[i], (nums[i-3] || 0) + nums[i])
        // so current number + 2 spaces before or current number + 3 spaces before 
        // so for first case when i = 2 nums[0]+nums[2] = 2+2 , nums[2-3] || 0 + nums[2] = 0+2
        // so nums[2] is set to 4 and nums = [2,1,4,1,5,2,1]

        //when i = 3  nums[1]+nums[3] = 1+1 , nums([3-3] || 0) + nums[3] = 2+1
        // so nums[3] is set to 3 and nums = [2,1,4,3,5,2,1]

        //when i = 4  nums[2]+nums[4] = 4+5 , nums([4-3] || 0) + nums[4] = 1+5
        // so nums[4] is set to 9 and nums = [2,1,4,3,9,2,1]

        //when i = 5  nums[3]+nums[5] = 3+2 , nums([5-3] || 0) + nums[5] = 4+2
        // so nums[5] is set to 6 and nums = [2,1,4,3,9,6,1]

        //when i = 6  nums[4]+nums[6] = 9+1 , nums([6-3] || 0) + nums[6] = 3+1
        // so nums[6] is set to 10 and nums = [2,1,4,3,9,6,10]

        nums[i] = Math.max(nums[i-2]+nums[i], (nums[i-3] || 0) + nums[i])
        console.log(nums)
    }
    return Math.max(nums[nums.length-1], nums[nums.length-2])

}

console.log(rob([2,1,2,1,5,2,1]))