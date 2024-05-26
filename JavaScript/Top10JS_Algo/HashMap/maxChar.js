// given a string , retunr the character that is most 
// commonly used in the string
// example
//maxChar("abccccccd") === "c"


function maxChar(str) {

    const hash = {}
    // Build the hash map
    for (let char of str) {
        if (hash[char]) {
            hash[char] += 1;
        } else {
            hash[char] = 1;
        }
    }
        // Find the character with the maximum frequency
        let maxCount = 0;
        let maxChar = '';
    
        for (let char in hash) {
            console.log(char , hash[char], "key and value in hash")
            if (hash[char] > maxCount) {
                maxCount = hash[char];
                maxChar = char;
            }
        }
    
        // for(const [key,value] of Object.entries(hash)){
        //     if (value > maxCount) {
        //         maxCount = value;
        //         maxChar = key;
        //     }
        // }
        return maxChar;

}

// console.log(maxChar("abccccccd"))
console.log(maxChar("apple 1231111"));