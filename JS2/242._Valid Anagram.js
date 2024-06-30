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

// second solution
var isAnagram2 = function(s, t) {
    debugger
    const map = new Map()
    for(const c of s){
        // Loop through each character `c` in the string `s`.
        const count = map.get(c) || 0;
        // Get the current count of the character `c` from the map. If the character is not found, default to 0.
        map.set(c , count+1)
        // Increment the count of the character `c` by 1 and update the map.
    }
    for(const c of t){
        // Loop through each character `c` in the string `t`.
        const count = map.get(c) || 0;
        // Get the current count of the character `c` from the map. If the character is not found, default to 0.
        map.set(c , count -1)
    }
    for ( const [keyPair,valuePair] of map.entries()){
        // Loop through each key-value pair `[keyPair,valuePair]` in the map.
        console.log([keyPair,valuePair])
        if (valuePair !== 0){
            // Check if the value `v` is not equal to 0.
            return false
        }
    }
    return true
}

// third solution
const isAnagram3 = function(s,t){

    let sSplit = s.split("").sort().join("")
    let tSplit = t.split("").sort().join("")
    console.log(sSplit,tSplit)
    return sSplit == tSplit
}

console.log(isAnagram2("anagram", "nagaram"))