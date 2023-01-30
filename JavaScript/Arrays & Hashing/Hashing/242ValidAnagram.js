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
  if(s.length !== t.length) return false
    let hash = {}
    let result = false
    let word1 = s.split("").sort();
    console.log(word1)
    hash[word1] =word1
    let word2 = t.split("").sort();
    console.log(word2)
    if(hash[word2]){
        hash[word1].push(word2)
        console.log("hash",hash)
      }
      else{
        hash[word2] =word2
        console.log("hash",hash)
      }
      if(Object.keys(hash).length == 1){
        console.log("Object.keys(hash)",Object.keys(hash))
        result = true
      }
      
     return result
};


// var isAnagram = function(s, t) {
//   if(s.length !== t.length) return false
//     let result = 0
//     let word1 = s.split("").sort();
//     console.log(word1)
//     let word2 = t.split("").sort();
//     console.log(word2)
//       for (i = 0; i < word1.length; i++){
//         if(word1[i] === word2[i]){
//           result = result + 1
//           console.log("result",result)
//         }
//         else(result = 0)
//       }

//       if(result == word1.length){
//         return true
//       }
//       else{return false}

// };


console.log(isAnagram("anagram","nagaram"))
console.log(isAnagram("car","rat"))
