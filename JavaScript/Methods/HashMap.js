var Hashmap = function(nums) {
    let hash = {}

    for(let i = 0; i < nums.length; i++){
        //if hash already exists push nums[i] into key
        if(hash[nums[i]]){
            hash[nums[i]].push(nums[i])
        }
        //else if hash does not exist set hash name with nums[i] = to nums[i]
        else{
            hash[nums[i]] = [nums[i]]
        }
    }
    let values = Object.values(hash)
    //gets values of the hashes
        console.log("values", values)
        values.map(x => console.log("map values",x))
    let keys = Object.keys(hash)
        console.log("keys ", keys )
        keys.map(x => console.log("map keys",x))
        console.log("hash", hash)
        return hash
};

console.log(Hashmap([1,1,1,2,2,3]))