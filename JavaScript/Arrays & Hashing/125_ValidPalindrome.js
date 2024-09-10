
// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.

 

// Example 1:

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.

function palindrome(s){
    // Convert the string to lowercase and filter out non-alphanumeric characters
    const filteredStr = s.toLowerCase().split('').filter((ch) => /^[a-z0-9]$/.test(ch));
    const reverseStr = [...filteredStr].reverse();

    // Compare the filtered string with its reversed version
    for (let i = 0; i < filteredStr.length; i++) {
        if (filteredStr[i] !== reverseStr[i]) {
            return false;
        }
    }
    return true;
    
}

console.log(palindrome("kayak"))
console.log(palindrome("madam"))
console.log(palindrome("caodingmoney"))
console.log(palindrome("A man, a plan, a canal: Panama"))
console.log(palindrome("race a car"))