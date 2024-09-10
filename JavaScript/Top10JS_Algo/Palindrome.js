

function palindrome(str){
    // Convert the string to lowercase and filter out non-alphanumeric characters
    const filteredStr = str.toLowerCase().split('').filter((ch) => /^[a-z0-9]$/.test(ch));
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