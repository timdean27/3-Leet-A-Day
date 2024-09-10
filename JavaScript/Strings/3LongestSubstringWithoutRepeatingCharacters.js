// Given a string s, find the length of the longest substring without repeating characters.

 

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


var lengthOfLongestSubstring = function(s) {
    let word = s.split("");
    let result = 0
    let chain = 0
    let last = ""
    for(let i = 0; i < word.length; i++) {
        console.log("word[i]",word[i], "last", last)

      
        if(word[i] != last){
            chain = chain + 1
            console.log("chain" ,chain)
            if(chain > result){
                result = chain
            }
            
        }
        else{chain = 0}
        last = word[i]
    }
    return result
};
console.log(lengthOfLongestSubstring("abcabcbb"))
// console.log(lengthOfLongestSubstring("bbbbbb"))
// console.log(lengthOfLongestSubstring("pwwkew"))