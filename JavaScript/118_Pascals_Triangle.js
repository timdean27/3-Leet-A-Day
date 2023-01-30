// Given an integer numRows, return the first numRows of Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

// Example 1:

// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

// Example 2:

// Input: numRows = 1
// Output: [[1]]

const generate = (numsRows) =>{
let answer = [];
if(numsRows >=1) answer.push([1])
if(numsRows >=2) answer.push([1,1])

    for(let i=2; i<numsRows; i++){
      let first = 1
      let last = 1

      let prev = answer[i-1]
      if(prev.length ===2){
        answer.push([first, first+last, last])
      }
      else{
        let left = 0
        let right = 0
        let add = []
while(right < prev.length){
    add.push(prev[left] + prev[right])
    left++
    right++
}
    answer.push([first, ...add, last])
      }
    }
return answer
}


console.log(generate(5))