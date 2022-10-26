// starting at a node you first travel to the deepest node you can reach
//pick a dirrection and travel in that dirrection as far ass possible before switching

//DFS uses a "stack" where you add and remove from the top


// const graph = {
//     a: ["b", "c"],
//     b: ["d"],
//     c: ["e"],
//     d: ["f"],
//     e: [],
//     f: [],
//   };

// if we start at "a" we pop off a from the stack and consider it the current node
//print a
// we push the neighbors 'b' and 'c' to the stack
//the stack still has data so we pop off the 'b' and this is current
//print b
// 'd' is now pushed into the stack (on top of c)
//so next iteration we pop off 'd' as current node
//print d
//'f' is now pushed into the stack
//'f' is then poped off but has no neighbors
//print f
//'c' now becomes the current node
//print c
//'e' is now pushed into the stack
//'e' is finally popped off
//print e

//printed: a,b,d,f,c,e



//implementation of DFT and print out nodes

const depthFirstPrint = (graph, source) => {
    // in DFT we want to use push and pop to manipulate just the end of the stack array
    // innitalize stack with source node
const stack = [source];

    // run algorithm while stack is not empty
    while (stack.length > 0) {
        // this will pop of the last stack element
        console.log("stack",stack)
        let current = stack.pop();
        console.log("stack",stack)
        console.log("current" ,current)
        console.log("graph[current]",graph[current])
        //BECAUSE THIS IS DFT
        //graph[current] is equal to the values inside the current key
        // so we are printing "a" and pushing in ['b', 'c']
        // next interation we pop out 'c' and push in ['e']
        // then pop of 'e' and push nothing
        //then pop out 'b' and push in ['d']
        //then pop out 'd' and push 'f'
        //finally pop 'f'
        
        // loop through graph starting at current node and gets next node
        for(let neighbor of graph[current]) {
            stack.push(neighbor)
        }
    }

}


const graph = {
    a: ["b", "c"],
    b: ["d"],
    c: ["e"],
    d: ["f"],
    e: [],
    f: [],
  };

depthFirstPrint(graph, 'a')