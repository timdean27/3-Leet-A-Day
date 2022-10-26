// starting at a node you first travel to the deepest node you can reach
//pick a dirrection and travel in that dirrection as far ass possible before switching

//DFS uses a "stack" where you add and remove from the top

const graph = {
  a: ["b", "c"],
  b: ["d"],
  c: [e],
  d: ["f"],
  f: [],
};

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
