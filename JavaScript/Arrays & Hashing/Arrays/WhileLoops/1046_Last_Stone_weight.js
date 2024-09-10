// You are given an array of integers stones where stones[i] is the weight of the ith stone.

// We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

// If x == y, both stones are destroyed, and
// If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
// At the end of the game, there is at most one stone left.

// Return the weight of the last remaining stone. If there are no stones left, return 0.

// Example 1:

// Input: stones = [2,7,4,1,8,1]
// Output: 1
// Explanation: 
// We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
// we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
// we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
// we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
// Example 2:

// Input: stones = [1]
// Output: 1



//will be alternating bettwen x and y and switching values based on results
//we need to chose the two heaviest avaliable stones
var lastStoneWeight = function(stones) {
    if (stones.length < 1) return 0
    if (stones.length === 1) return stones[0]

    let x = 0
    let y = 0
   while (stones.length >1) {
    stones.sort((a, b)=> a - b)
    console.log("stones 1" ,stones)
    y = stones[stones.length - 1]
    console.log("y",y)
    stones.pop()
    x = stones[stones.length - 1]
    console.log("x",x)
    stones.pop()
    console.log("stones 2" ,stones)
    if(x === y){
        console.log("x = y")
    }
    else{
        let z = y-x
        console.log("z",z)
        stones.push(z)
    }
    console.log("stones 3" ,stones)
   }

   if (stones.length === 1) return stones[0]
   else return 0
};

console.log(lastStoneWeight([2,7,4,1,8,1]))