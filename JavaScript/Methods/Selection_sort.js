
const sortFunc =(nums)=>{

    for (let i=0; i< nums.length; i++){
        let minIndex = i;

        for (let j= i+1; j< nums.length; j++){
            if(nums[j] < nums[minIndex]){
                minIndex = j; 
            }
        }
        [nums[i], nums[minIndex]] = [nums[minIndex], nums[i]]
    }
        return nums
}



console.log(sortFunc([2,4,3,6,5,1]))