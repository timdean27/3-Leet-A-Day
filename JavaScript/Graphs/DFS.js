
// how DFS works in JavaScript:
// Stack: DFS uses a stack data structure to keep track of nodes to visit. 
// JavaScript arrays can be used as stacks because they support the push() and pop() operations, which allow items to be added or removed from the end of an array, mimicking a stack.

// Recursive Approach or Iterative Approach with Stack: DFS can be implemented 
// using either recursion or iteration (with an explicit stack). In JavaScript, both approaches are feasible.

// Recursive Approach: In this approach, a function calls 
// itself to explore each neighbor of a node recursively until all nodes have been visited.

// Iterative Approach with Stack: In this approach, a stack is explicitly maintained to keep track of nodes to visit. 
// The algorithm iteratively pops nodes from the stack, explores their neighbors, and pushes unvisited neighbors onto the stack.


// Graph represented as an adjacency list
const graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
};

// Function to perform DFS recursively
const dfsRecursive = (node, visited, graph) => {
    if (!visited[node]) {
        visited[node] = true;
        console.log("Visited node:", node);
        // Explore neighbors recursively
        graph[node].forEach(neighbor => dfsRecursive(neighbor, visited, graph));
    }
};

// Function to perform DFS traversal
const dfsTraversal = (startNode, graph) => {
    const visited = {};
    dfsRecursive(startNode, visited, graph);
};

// Perform DFS traversal starting from node 'A'
dfsTraversal('A', graph);
