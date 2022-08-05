// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters 
// of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

var isAnagram = function(s, t) {
    let hash = {}
    let result = false
    let word1 = s.split("").sort();
    hash[word1] =word1
    let word2 = t.split("").sort();
    if(hash[word2]){
        hash[word1].push(word2)
      }
      else{
        hash[word2] =word2
      }
      if(Object.keys(hash).length == 1){
        result = true
      }
     return result
};
console.log(isAnagram("anagram","nagaram"))
