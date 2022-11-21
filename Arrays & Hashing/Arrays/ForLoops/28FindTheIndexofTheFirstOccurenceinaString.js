// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
// or -1 if needle is not part of haystack.

 

// Example 1:

// Input: haystack = "sadbutsad", needle = "sad"
// Output: 0
// Explanation: "sad" occurs at index 0 and 6.
// The first occurrence is at index 0, so we return 0.
// Example 2:

// Input: haystack = "leetcode", needle = "leeto"
// Output: -1
// Explanation: "leeto" did not occur in "leetcode", so we return -1.


var strStr = function(haystack, needle) {
    
    let result = [-1]
    for(let i = 0; i < haystack.length; i++) {
        // console.log(haystack[i])
        if(haystack[i] === needle[0]){
            let currentStreak = 1
            for(let j = 0; j < needle.length; j++) {
                if(haystack[i+j] === needle[j]){
                    console.log(haystack[i+j] ,needle[j])
                    console.log(currentStreak)
                    if(currentStreak === needle.length){result.push(i)}
                    currentStreak ++
                }
                else{ currentStreak = 0}
            }
        }
    }
    if(result.length > 1){
        return result[1]
    }
    else{ return result[0] }
};

console.log(strStr("sadbutsad","sad"))
//console.log(strStr("leetcode","leeto"))
// console.log(strStr("babba","bbb"))
// console.log(strStr("mississippi","issip"))