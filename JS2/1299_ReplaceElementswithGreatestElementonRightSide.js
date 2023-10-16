// Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

// After doing so, return the array.

 

// Example 1:

// Input: arr = [17,18,5,4,6,1]
// Output: [18,6,6,6,1,-1]
// Explanation: 
// - index 0 --> the greatest element to the right of index 0 is index 1 (18).
// - index 1 --> the greatest element to the right of index 1 is index 4 (6).
// - index 2 --> the greatest element to the right of index 2 is index 4 (6).
// - index 3 --> the greatest element to the right of index 3 is index 4 (6).
// - index 4 --> the greatest element to the right of index 4 is index 5 (1).
// - index 5 --> there are no elements to the right of index 5, so we put -1.
// Example 2:

// Input: arr = [400]
// Output: [-1]
// Explanation: There are no elements to the right of index 0.

var replaceElements = function(arr) {
let newArry = []
let max = -1

//loop through backwords so the largest value to the "right" is just the next largest value not worrying about checking whats further right
for(let i = arr.length-1 ; i >= 0 ; i --){
    console.log(i,"i")
    newArry[i] = max // set the current value of max to the newArry[i] doing this first will always make last value -1
    console.log(max, " current max before reset")
    max = Math.max(max, arr[i])// set the value of max to the current valeu or the current arr value
    console.log(max, "max value after reset")
}

return newArry
};

console.log(replaceElements([17, 18, 5, 4, 6, 1]));
// answer [18,6,6,6,1,-1]




