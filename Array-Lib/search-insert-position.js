var searchInsert = function(nums, target) {
    for(let x = 0 ; x < nums.length; x++){
        if(target <= nums[x]){
            return x
        }    
    }
     return nums.length
};

console.log(searchInsert([1,3,5,6],5))
console.log(searchInsert([1,3,5,6],2))
console.log(searchInsert([1,3,5,6],7))