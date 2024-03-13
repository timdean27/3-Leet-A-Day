// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }

    const sHash = {};
    const tHash = {};

    for (let letter of s) {
        if (sHash[letter]) {
            sHash[letter]++;
        } else {
            sHash[letter] = 1;
        }
    }

    for (let letter of t) {
        if (tHash[letter]) {
            tHash[letter]++;
        } else {
            tHash[letter] = 1;
        }
    }

    // Compare the character frequencies in sHash and tHash
    for (let char in sHash) {
        console.log(`sHash[char] ${sHash[char]}`, `tHash[char] ${tHash[char]}`, `char ${char}`)
        if (sHash[char] !== tHash[char]) {
            return false;
        }
    }

    return true;
};

// console.log(isAnagram("rat", "car")); 


const isAnagram2 = function(s,t){

    let sSplit = s.split("").sort().join("")
    let tSplit = t.split("").sort().join("")
    console.log(sSplit,tSplit)
    return sSplit == tSplit
}

console.log(isAnagram2("anagram", "nagaram"))