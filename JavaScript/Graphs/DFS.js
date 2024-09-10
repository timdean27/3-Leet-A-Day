
// how DFS works in JavaScript:
// Stack: DFS uses a stack data structure to keep track of nodes to visit. 
// JavaScript arrays can be used as stacks because they support the push() and pop() operations, which allow items to be added or removed from the end of an array, mimicking a stack.

// Recursive Approach or Iterative Approach with Stack: DFS can be implemented 
// using either recursion or iteration (with an explicit stack). In JavaScript, both approaches are feasible.

// Recursive Approach: In this approach, a function calls 
// itself to explore each neighbor of a node recursively until all nodes have been visited.

// Iterative Approach with Stack: In this approach, a stack is explicitly maintained to keep track of nodes to visit. 
// The algorithm iteratively pops nodes from the stack, explores their neighbors, and pushes unvisited neighbors onto the stack.

//    A
//   / \
//  B   C
// /|   |
// D E  F

// Node 'A' is connected to nodes 'B' and 'C'.
// Node 'B' is connected to nodes 'A', 'D', and 'E'.
// Node 'C' is connected to nodes 'A' and 'F'.
// Node 'D' is connected to node 'B'.
// Node 'E' is connected to nodes 'B' and 'F'.
// Node 'F' is connected to nodes 'C' and 'E'.
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
// This function takes three parameters: 
// the current node, the set of visited nodes, and the graph.
// It checks if the current node hasn't been visited yet. 
// If not, it marks it as visited, logs it, 
// and then recursively calls itself for each 
// unvisited neighbor.


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

// This function also takes two parameters: 
// the starting node and the graph.
// It initializes an empty set of visited nodes
// and a stack with the starting node.
// It iterates until the stack is empty, 
// popping the top node from the stack each time.
// If the popped node hasn't been visited yet, 
// it marks it as visited, logs it,
// and pushes its unvisited neighbors onto the stack.

// Perform DFS traversal starting from node 'A' using both methods
console.log("Recursive DFS:");
dfsRecursive('A', {}, graph);

console.log("\nIterative DFS:");
dfsIterative('A', graph);
// iterative DFS algorithm 
// Here's what happens in each run:

// First Iteration:

// Stack: ['A']
// Pop 'A' from the stack.
// Mark 'A' as visited.
// Log: "Visited node (Iterative): A"
// Push unvisited neighbors of 'A' onto the stack: ['C', 'B']
// Second Iteration:

// Stack: ['C', 'B']
// Pop 'B' from the stack.
// Mark 'B' as visited.
// Log: "Visited node (Iterative): B"
// Push unvisited neighbors of 'B' onto the stack: ['D', 'E', 'A']
// Third Iteration:

// Stack: ['C', 'D', 'E', 'A']
// Pop 'A' from the stack.
// 'A' has been visited before, so it's skipped.
// Fourth Iteration:

// Stack: ['C', 'D', 'E']
// Pop 'E' from the stack.
// Mark 'E' as visited.
// Log: "Visited node (Iterative): E"
// Push unvisited neighbors of 'E' onto the stack: ['F', 'B']
// Fifth Iteration:

// Stack: ['C', 'D', 'F', 'B']
// Pop 'B' from the stack.
// 'B' has been visited before, so it's skipped.
// Sixth Iteration:

// Stack: ['C', 'D', 'F']
// Pop 'F' from the stack.
// Mark 'F' as visited.
// Log: "Visited node (Iterative): F"
// Push unvisited neighbors of 'F' onto the stack: ['E', 'C']
// Seventh Iteration:

// Stack: ['C', 'D', 'C']
// Pop 'C' from the stack.
// 'C' has been visited before, so it's skipped.
// Eighth Iteration:

// Stack: ['C', 'D']
// Pop 'D' from the stack.
// Mark 'D' as visited.
// Log: "Visited node (Iterative): D"
// Push unvisited neighbors of 'D' onto the stack: ['B']
// Ninth Iteration:

// Stack: ['C', 'B']
// Pop 'B' from the stack.
// 'B' has been visited before, so it's skipped.
// Tenth Iteration:

// Stack: ['C']
// Pop 'C' from the stack.
// 'C' has been visited before, so it's skipped.
// End of Traversal:
// The stack is empty, so the traversal ends.