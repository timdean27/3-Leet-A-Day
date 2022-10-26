// starting at a node we go through the first options(dirrect) nodes first
//you would explore all immediate neighbors and keep applying that behavior evenly

//BFT uses a "Queue" add to the back and remove form the front

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
  // 'd' is now pushed to the back of the stack
  //'c' now becomes the current node
  //print c
  //'e' is now pushed to the back of the stack
  //so next iteration we pop off 'd' as current node
  //print d
  //'f' is now pushed to the back of the stack
  //we pop off 'e' as current node with no neighbors
  //print e
  //'f' is then poped off but has no neighbors
  //print f

  //printed: a,b,c,d,e,f