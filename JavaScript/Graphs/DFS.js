
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

// Recursive DFS traversal function
const dfsRecursive = (node, visited, graph) => {
    if (!visited[node]) {
        visited[node] = true;
        console.log("Visited node (Recursive):", node);
        // Explore neighbors recursively
        graph[node].forEach(neighbor => dfsRecursive(neighbor, visited, graph));
    }
};

// Iterative DFS traversal function
const dfsIterative = (startNode, graph) => {
    const visited = {};
    const stack = [startNode]; // Initialize stack with start node

    while (stack.length > 0) {
        const currentNode = stack.pop(); // Pop the top node from the stack

        // If node has not been visited yet, mark it as visited and explore its neighbors
        if (!visited[currentNode]) {
            visited[currentNode] = true;
            console.log("Visited node (Iterative):", currentNode);

            // Push unvisited neighbors onto the stack
            graph[currentNode].forEach(neighbor => {
                if (!visited[neighbor]) {
                    stack.push(neighbor);
                }
            });
        }
    }
};

// Perform DFS traversal starting from node 'A' using both methods
console.log("Recursive DFS:");
dfsRecursive('A', {}, graph);

console.log("\nIterative DFS:");
dfsIterative('A', graph);

