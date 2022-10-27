// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
// You may assume all four edges of the grid are all surrounded by water.

// Example 1:

// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1
// Example 2:

// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3


const getAdjNeighbors = (i,j,grid,visited) =>{
    const adjNeighbors = [];

    if(i > 0 && !visited[i -1][j]){
        adjNeighbors.push([i-1, j])
    }
    if(i < grid.length -1 && !visited[i +1][j]){
        adjNeighbors.push([i+1, j])
    }
    if(j > 0 && !visited[i][j-1]){
        adjNeighbors.push([i, j-1])
    }
    if(j < grid.length -1 && !visited[i][j-1]){
        adjNeighbors.push([i, j+1])
    }

    return adjNeighbors
}



const dFS = (i,j,grid,visited) =>{
    const stack = [[i,j]];
    let islandSize = 0

    while(stack.length){
        let currentNode = stack.pop();
        let [i,j] = currentNode;

        //check is visited
        if(visited[i][j]) continue;
        visited[i][j] = true;

        //check if cell is part of an island
        if(grid[i][j] === '0') continue;
        islandSize++;

        let adjNeighbors = getAdjNeighbors(i,j,grid,visited);
        stack.push(...adjNeighbors);
    }

    return islandSize > 0 ? true : false;
}

const numIslands = (grid) => {

    const visited = grid.map(row => row.map(cell => false));
    console.log(visited)
    let islandCount = 0;

    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[i].length; j++){
            if(dFS(i,j,grid,visited)) islandCount++;

        }
    }


};
console.log(
  numIslands(
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
  )
);
