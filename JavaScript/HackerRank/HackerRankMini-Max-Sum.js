function miniMaxSum(arr) {
    arr.sort((a,b) =>a-b)

    let sum = 0
    for(let i = 0; i < arr.length; i++) {
    sum = sum + arr[i]
    //    console.log(sum)
    }
    let min = sum - arr[arr.length-1]
    let max = sum - arr[0]
    console.log(min , max)
}

miniMaxSum([1,3,5,7,9])