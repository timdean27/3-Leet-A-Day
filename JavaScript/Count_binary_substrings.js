// Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

// Substrings that occur multiple times are counted the number of times they occur.

 

// Example 1:

// Input: s = "00110011"
// Output: 6
// Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
// Notice that some of these substrings repeat and are counted the number of times they occur.
// Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.


var countBinarySubstrings = function(s) {
    let res = 0;
    for(let i = 0; i < s.length; i++) {
        if(s[i] == '1'){
 
            for(let j = i+1; j < s.length; j++) {
                if(s[j] == '1')
                res++
            }
        }
    }
    return res;
};


console.log(countBinarySubstrings('00110011'))

