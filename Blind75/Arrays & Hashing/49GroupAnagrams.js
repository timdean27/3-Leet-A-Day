// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
// typically using all the original letters exactly once.


// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Example 2:

// Input: strs = [""]
// Output: [[""]]
// Example 3:

// Input: strs = ["a"]
// Output: [["a"]]

var groupAnagrams = function(strs) {
    let hash = {}
    for(let i = 0; i < strs.length; i++) {
        let word = strs[i].split("").sort();
        //split word to letters and sort

        //if (word) is a key in hash than we push the currnt strs[i] to that array with that key 
      //if key already exists 'a,e,t' then pushes "tea" , "ate"
      if(hash[word]){
        hash[word].push(strs[i])
      }

              // so will creat key 'a,e,t' and push :"eat" on first iteration
      else{
        hash[word] =[strs[i]]
      }
    }
    // console.log(hash)
    //  {
    //     'a,e,t': [ 'eat', 'tea', 'ate' ],
    //     'a,n,t': [ 'tan', 'nat' ],
    //     'a,b,t': [ 'bat' ]
    //   }
    const keys = Object.keys(hash);
    // console.log(keys)
    // [ 'a,e,t', 'a,n,t', 'a,b,t' ]
    const values = keys.map(function(v) { return hash[v]})
    //maps through keys and returns the arrays contained
    // [ [ 'eat', 'tea', 'ate' ], [ 'tan', 'nat' ], [ 'bat' ] ]
    return values
    
};

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))