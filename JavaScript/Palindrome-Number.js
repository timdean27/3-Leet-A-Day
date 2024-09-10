// this answer sucks but it works
//PASS

// var isPalindrome = function(x) {
//     let array = (""+x).split("");
//     console.log(array)
//     let reverse = []
//     let final = []
//     for (let i = 0; i < array.length; i++){
//         if(array[0] != '-'){
//         console.log(array[(array.length-1)-i])
//         reverse.push(array[(array.length-1)-i])
//         console.log(reverse)
//         }
//         else{return false}
//     }

//     for (let j = 0; j < array.length; j++){
//         if ((array[j]) == reverse[j]){
//             final.push(array[(array.length-1)-j])
//         }
        
//     }
//     if(final.length == array.length){
//         return true
//     }
//     else{return false}
   
// };



var isPalindrome = function(s) {
    let forward = (""+s);
    let reverse = forward.split('').reverse().join('')
    if (forward !== reverse){
        return false
    } return true
    
        
    };
console.log(isPalindrome(121))
console.log(isPalindrome(123))
console.log(isPalindrome(-121))