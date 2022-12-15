// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

// Example 1:

// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps
// Example 2:

// Input: n = 3
// Output: 3
// Explanation: There are three ways to climb to the top.
// 1. 1 step + 1 step + 1 step
// 2. 1 step + 2 steps
// 3. 2 steps + 1 step


var climbStairs = function(n) {
  let dp = []
  dp[1] = 1
  dp[2] = 2
  for(let i = 3; i <= n; i++){
    // the way to get to the step i is going to be the solution to get to previous(i-1) + solution to get to previous-1(i-2)
    dp[i] = dp[i-1] + dp[i-2]
    console.log("i",i)
    console.log("dp[i]",dp[i])
    console.log("dp[i-1]",dp[i-1])
    console.log("dp[i-2]",dp[i-2])
  }
  return dp[n]
};

console.log(climbStairs(6))
// console.log(climbStairs(2))
// console.log(climbStairs(3))