// There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for 
// room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

// When you visit a room, you may find a set of distinct keys in it. 
// Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

// Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
// return true if you can visit all the rooms, or false otherwise.

 

// Example 1:

// Input: rooms = [[1],[2],[3],[]]
// Output: true
// Explanation: 
// We visit room 0 and pick up key 1.
// We then visit room 1 and pick up key 2.
// We then visit room 2 and pick up key 3.
// We then visit room 3.
// Since we were able to visit every room, we return true.
// Example 2:

// Input: rooms = [[1,3],[3,0,1],[2],[0]]
// Output: false
// Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

var canVisitAllRooms = function(rooms) {
    let vis = [1], 
    stack = [0], 
    count = 1
 
    while (stack.length) {
        let keys = rooms[stack.pop()]
        console.log("key", keys)
        for (let k of keys){
            if (!vis[k]) {
                stack.push(k)
                vis[k] = 1 
                count++
                console.log("stack" ,stack)
            }
            
        }
    }
    return rooms.length === count
};

// console.log(canVisitAllRooms([[1],[2],[3],[]]))
// console.log(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
// console.log(canVisitAllRooms([[1,2],[2,1],[1]]))
console.log(canVisitAllRooms([[1,3],[1,4],[2,3,4,1],[],[4,3,2]]))
// we start where stack = [0]
// so rooms[0] = keys = [1,3]
// in for looop vis[k] is vis[1] undifined 
// so push 1 to stack
//next vix[3] undifined push 3 to stack
// exit for loop and check keys = rooms[3] = []
//next check keys = rooms[1] = [1,4]
//for loop vis[4] undifined push 4 to stack
//for loop vis[1] = not empty so skip 
//next check keys = rooms[4] = [4,3,2]
// for loop vis[2] push 2 to stack
// for loop vis[3] = not empty so skip
// for loop vis[4] = not empty so skip
//next check keys = rooms[2] = [ 2, 3, 4, 1 ]
// all not empty skip
//count == rooms.length to return true