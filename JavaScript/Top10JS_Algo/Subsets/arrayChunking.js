//Given an array and chunk size, divide the array into many subarrays
// were each subarray is of length size

// Chunk([1,2,3,4],2) --> [[1,2] , [3,4]]
// Chunk([1,2,3,4,5],2) -> [[1,2] , [3,4], [5]]

function Chunker(arry , k){
    const result = []
    let index = 0
    while(index< arry.length){
        console.log(index)
    result.push(arry.slice(index,index+k))

    index += k
    }
    return result

}

console.log(Chunker([1,2,3,4,5],2))