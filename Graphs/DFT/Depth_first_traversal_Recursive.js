const depthFirstPrint = (graph, source) => {
// soruce node is current location
console.log("source",source)
//look at source neighbors

// first source prints 'a'
//graph[source] is ['b', 'c']
//neighbor is set to 'b' and the main function is called again
//graph[source] is [ 'd' ]
//neighbor is set to 'd' and the main function is called again
//graph[source] is [ 'f' ]
//neighbor is set to 'f' and the main function is called again
//graph[source] [] which means the main function is not called
// neighbor is set to c and the main function is called again
//graph[source] is [ 'e' ]
// neighbor is set to e and the main function is called again
//graph[source] is []
//and graph loop is ended
console.log("graph[source]",graph[source])
for(let neighbor of graph[source]){
  console.log("neighbor",neighbor)
    depthFirstPrint(graph , neighbor)
    
}

}


const graph = {
    a: ["b", "c"],
    b: ["d"],
    c: ["e"],
    d: ["f"],
    e: [],
    f: [],
    z:[],
  };

depthFirstPrint(graph, 'a')