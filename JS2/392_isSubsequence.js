// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

// Example 1:

// Input: s = "abc", t = "ahbgdc"
// Output: true
// Example 2:

// Input: s = "axc", t = "ahbgdc"
// Output: false
 

// Constraints:

// 0 <= s.length <= 100
// 0 <= t.length <= 104
// s and t consist only of lowercase English letters.


var isSubsequence = function(s, t) {
    let sAry = s.split("");
    let tAry = t.split("");
    let count = 0;
    let answer = false; 
    
    if(s == ""){
        return true
    }
    if (sAry.length > tAry.length) {
        return answer;
    }

    for (let i = 0; i < tAry.length; i++) {
        if (sAry[count] === tAry[i]) {
            count += 1;
        }
        if (count === sAry.length) {
            answer = true;
            break; // If we found a match, we don't need to continue checking
        }
    }

    return answer;
};

console.log(isSubsequence("", ""));


