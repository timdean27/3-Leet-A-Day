// Write a function that reverses a string.
//The input string is given as an array of characters s.

// You must do this by modifying the input
//array in-place with O(1) extra memory.

// Example 1:

// Input: s = ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]
// Example 2:

// Input: s = ["H","a","n","n","a","h"]
// Output: ["h","a","n","n","a","H"]

// var reverseString = function (s) {
//     return s.reverse();
// };

function reverse(s) {
    let reversed = [...s];
    let start = 0
    for (let i = reversed.length - 1; i >= 0; i--) {
      s[start] = reversed[i];
      start++
    }
    return s
}

console.log(reverse(["h","e","l","l","o"]));
