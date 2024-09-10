// Write a function, hasPath, that takes in an object representing the adjacency list of a directed acyclic graph and two nodes (src, dst). 
// The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.



//we take in a source(starting point)
//and a destination(eding point)
//return if we can get to the ending node from the starting node

const hasPath = (graph, src, dst) => {
    const stack = [src]
    let result = false
    while (stack.length > 0){
        console.log("stack",stack)
        let current = stack.pop()
        console.log("current", current)
        for(let neighbor of graph[current]){
            console.log("neighbor", neighbor)
            stack.push(neighbor)
            if(neighbor === dst){result = true}
        }
    }
    return result
}

// test_00:
const graph = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: []
  };
console.log(hasPath(graph, 'f', 'k')); // true

//   test_01:
const graph1 = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: []
  };
  
console.log(hasPath(graph1, 'f', 'j')); // false


//   test_02:
  const graph2 = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: []
  };
  
console.log(hasPath(graph2, 'i', 'h')); // true

  
//   test_03:
  const graph3 = {
    v: ['x', 'w'],
    w: [],
    x: [],
    y: ['z'],
    z: [],  
  };
  
console.log(hasPath(graph3, 'v', 'w')); // true

  
//   test_04:
  const graph4 = {
    v: ['x', 'w'],
    w: [],
    x: [],
    y: ['z'],
    z: [],  
  };


console.log(hasPath(graph4, 'v', 'z')); // false