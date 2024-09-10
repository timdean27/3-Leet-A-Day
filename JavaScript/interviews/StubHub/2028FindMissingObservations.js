// You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

// You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

// Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

// The average value of a set of k numbers is the sum of the numbers divided by k.

// Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.


function missingRolls(A, M , F){
// if reaming number of rolls can not add up to remaing averge return [0].
//exapmle if avg remaing = 3 and have F =4 dice, or if avg = 14 and have f+2 dice 

// when finding solutions we cant take the reaming avergae under 0

let length = A.length
let sum = 0
let missingDice=[]
for(let i = 0; i < length; i++){
 sum = sum + A[i]
}
console.log(sum)
let remainingAVG = ((M *(length + F)) - sum)
console.log("remainingAVG",remainingAVG)
// this will give us the remaing Average that the F dice must add to
// solve for outlier cases where F dice cant equal averag
if(remainingAVG < F || remainingAVG > F * 6){
    return []
}

while (remainingAVG > 0){
    // the largest value we can remove is going to be the min of 6
    // or the remaining average - remaining dice + 1(always leaving 1 for next dice)
    let currentDice = Math.min(6, remainingAVG - F + 1)
    missingDice.push(currentDice)
    // remove value from average and F
    F = F-1
    remainingAVG = (remainingAVG - currentDice)
}

return missingDice
    
}



// var missingRolls = function(rolls, mean, n) {
//     let expectedTotal = (rolls.length + n) * mean;
//     let total = 0;
//     let remainder = 0;
//     let output = []
//     rolls.forEach(roll => {
//         total += roll;
//     })
//     if(total + (6 * n) < expectedTotal || total + (1 * n) > expectedTotal) return output;
//     const remainingToBeAdded = (expectedTotal - total) / n;
//     console.log("remainingToBeAdded",remainingToBeAdded)
//     while(n) {
//         let wholeNumber = Math.floor(remainingToBeAdded)
       
//         remainder += (remainingToBeAdded - wholeNumber);
//         console.log("remainder",remainder);
//         if(remainder >= 1) {
//             wholeNumber++;
//             remainder--;
//         }
//         console.log("wholeNumber",wholeNumber);
//         n--;
//         // if(!n && remainder > 0.999) wholeNumber++;
//         output.push(wholeNumber);
//     }
//     return output;
// };

// console.log(missingRolls([3,2,4,3],4,2))
// console.log(missingRolls([1,5,6],3,4))
console.log(missingRolls([4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5],4,40))
//M is the mean of all dice rolled
//F is the missing dice rolls
//from example if we have 4 rolls and F = 2 M = 4
//this means we have 6 dice rolled and can get the total value the must ad to
// by multiplying 6*M in this case 6*4=24
// sum of given dice [3,2,4,3] = 12 
//24 - 12 = 12 and F = 2 so remaiing dice must add to 12