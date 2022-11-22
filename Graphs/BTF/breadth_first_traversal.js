// starting at a node we go through the first options(dirrect) nodes first
//you would explore all immediate neighbors and keep applying that behavior evenly

//BFT uses a "Queue" add to the back and remove form the front


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



const breadthFirstPrint = (graph, source) =>{
  const queue = [source];
   // we will use array.shift() to remvoe the first element
   //queue.push() will add to the back of the array
   while(queue.length >0){
    let current = queue.shift();
    console.log(current);
    console.log("graph[current]", graph[current])
    for(let neighbor of graph[current]){
      console.log("neighbor", neighbor);
      queue.push(neighbor);
      console.log("queue", queue)
    }
   }
  //current is set to a and shifted out of queue
  //graph[current] is ['b', 'c']
  //neighbor is to b and pushed to queue
  //queue [ 'b' ]
  //neighbor is set to c and pushed to queue
  //queue is set[ 'b', 'c' ]
  //current is set to b and shifted out of queue
  //neighbor d and pushed to queue
  //queue [ 'c', 'd' ]
  //current is set to c and shifted out of queue
  //neighbor e and pushed to queue
  //queue [ 'd', 'e' ]
  //current is set to d and shifted out of queue
  //neighbor f and pushed to queue
  //queue [ 'e', 'f' ]
  //current is set to e and shifted out of queue
  //neighbor is []
  //queue [ 'f']
  //current is set to f and shifted out of queue
}

  const graph = {
    a: ["b", "c"],
    b: ["d"],
    c: ["e"],
    d: ["f"],
    e: [],
    f: [],
  };
  breadthFirstPrint(graph,'a')