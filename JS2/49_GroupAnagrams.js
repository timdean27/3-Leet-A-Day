// Given an array of strings strs, group the anagrams together. You can return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

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
    let mainhash = {};

    for (let i = 0; i < strs.length; i++) {
        const sortedStr = strs[i].split('').sort().join('');
        
        if (mainhash[sortedStr]) {
            mainhash[sortedStr].push(strs[i]);
        } 
        else {
            mainhash[sortedStr] = [strs[i]]; 
        }
    }

    const result = Object.values(mainhash); // Convert the values of the object to an array
    return result;
};

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))