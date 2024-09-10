// Given a string s and an integer k, 
// reverse the first k characters for every 
// 2k characters counting from the start of the string.

// If there are fewer than k characters left, 
// reverse all of them. If there are less than 
// 2k but greater than or equal to k characters, 
// then reverse the first k characters and 
// leave the other as original.

 

// Example 1:

// Input: s = "abcdefg", k = 2
// Output: "bacdfeg"
// Example 2:

// Input: s = "abcd", k = 2
// Output: "bacd"


// var reverseStr = function(s, k) {
//     const strToArry = s.split("");


//     for (let i = 0; i <strToArry.length; i += 2 * k) {
//         let start = i;
//         let end = Math.min(i + k - 1, strToArry.length - 1);

//         // Reverse the segment from start to end
//         while (start < end) {
//             [strToArry[start], strToArry[end]] = [strToArry[end], strToArry[start]];
//             start++;
//             end--;
//         }
//     }

//     return strToArry.join("");
// };

// console.log(reverseStr("abcdefgh", 2))


var reverseStr = function(s, k) {
    let arr = s.split(''); // Convert the string to an array


for (let i = 0; i < arr.length; i += 2 * k) {
 // Get the segment to reverse
 let segment = arr.slice(i, i + k);
 // Reverse the segment
 segment.reverse();
// Insert the reversed segment back into the array
for (let j = 0; j < segment.length; j++) {
        arr[i + j] = segment[j];
    }
}

return arr.join('');
};

console.log(reverseStr("abcdefgh", 2))