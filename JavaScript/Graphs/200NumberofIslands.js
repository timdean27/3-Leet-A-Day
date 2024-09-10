// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

// Example 1:

// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1

// Depth-first search function to find connected islands starting from cell (i, j)
const dFS = (i, j, grid, visited) => {
    // Initialize a stack to keep track of cells to be visited
    const stack = [[i, j]];
    // Initialize island size counter
    let islandSize = 0;

    // Continue DFS until stack is empty
    while (stack.length) {
        // Pop the last element from the stack
        let curNode = stack.pop();

        // Extract row and column indices of the current cell
        let [i, j] = curNode;

        // Check if the current cell has been visited, if so, skip
        if (visited[i][j]) continue;
        // Mark the current cell as visited
        visited[i][j] = true;

        // Check if the current cell is part of an island
        if (grid[i][j] === "0") continue;
        // Increment island size counter
        islandSize++;

        // Get adjacent unvisited neighbors of the current cell
        let adjNeighbors = getAdjNeighbors(i, j, grid, visited);

        // Push adjacent neighbors to the stack for further exploration
        stack.push(...adjNeighbors);
    }

    // Return true if any part of the grid was part of an island, otherwise false
    return islandSize > 0;
};

// Function to get adjacent unvisited neighbors of a cell (i, j)
const getAdjNeighbors = (i, j, grid, visited) => {
    // Initialize an array to store adjacent neighbors
    const adjNeighbors = [];

    // Check if the cell above is a valid neighbor and unvisited
    if (i > 0 && !visited[i - 1][j]) {
        adjNeighbors.push([i - 1, j]);
    }
    // Check if the cell below is a valid neighbor and unvisited
    if (i < grid.length - 1 && !visited[i + 1][j]) {
        adjNeighbors.push([i + 1, j]);
    }
    // Check if the cell to the left is a valid neighbor and unvisited
    if (j > 0 && !visited[i][j - 1]) {
        adjNeighbors.push([i, j - 1]);
    }
    // Check if the cell to the right is a valid neighbor and unvisited
    if (j < grid[0].length - 1 && !visited[i][j + 1]) {
        adjNeighbors.push([i, j + 1]);
    }

    // Return array of adjacent unvisited neighbors
    return adjNeighbors;
};

// Function to count the number of islands in the grid
var numIslands = function (grid) {
    // Create a 2D array to track visited cells, initialized with false
    const visited = grid.map(row => row.map(cell => false));
    // Initialize island count
    let islandCount = 0;

    // Iterate through each cell in the grid
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            // If the current cell is part of an island, increment island count
            if (dFS(i, j, grid, visited)) {
                islandCount++;
            }
        }
    }

    // Return the total number of islands found
    return islandCount;
};

// Test the function with a sample grid and output the result
console.log(numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]));
