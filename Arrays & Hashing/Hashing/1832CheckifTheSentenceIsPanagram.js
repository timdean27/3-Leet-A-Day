// A pangram is a sentence where every letter of the English alphabet appears at least once.

// Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

// Example 1:

// Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
// Output: true
// Explanation: sentence contains at least one of every letter of the English alphabet.
// Example 2:

// Input: sentence = "leetcode"
// Output: false

//hashmap
var checkIfPangram = function(sentence) {
    //english alphabet contains 26 letters
    // mak each one a key and check key length, if not 26 return false
    let hash = {};
    let word = sentence.split("").sort();
    // console.log(word)

    // will only make key if it doesnt already exist 
    for (let i = 0; i < word.length; i++) {
        hash[word[i]] =word[i]
    }

    return Object.keys(hash).length == 26
};


console.log(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
console.log(checkIfPangram("leetcode"))