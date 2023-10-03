// Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

// Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

// a, b are from arr
// a < b
// b - a equals to the minimum absolute difference of any two elements in arr
 

// Example 1:

// Input: arr = [4,2,1,3]
// Output: [[1,2],[2,3],[3,4]]
// Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
// Example 2:

// Input: arr = [1,3,6,10,15]
// Output: [[1,3]]
// Example 3:

// Input: arr = [3,8,-10,23,19,-4,-14,27]
// Output: [[-14,-10],[19,23],[23,27]]


var minimumAbsDifference = function(arr) {
        let minDif = Infinity
        arr.sort((a,b)=>(a-b))
        console.log(arr)
        let result = []
        //find the minimum absolute difference
        for(let i=0; i<arr.length; i++){
            let newdifference = arr[i+1] - arr[i]
            if(newdifference < minDif){
                minDif = newdifference
                console.log(minDif)
                result = [[arr[i], arr[i+1]]]
            }
            else if (newdifference == minDif)
            {
                result.push([arr[i], arr[i+1]])
            }
        }
 return result
};
console.log(minimumAbsDifference([4,2,1,3]))