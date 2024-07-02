// Given an integer n, return a counter function. 
// This counter function initially returns n and 
// then returns 1 more than the previous value 
// every subsequent time it is called 
// (n, n + 1, n + 2, etc).

 

const createCounter = function(n) {
    let count = n;
    return function() {
        return count++; //count is retunred and then incremented
    };
};


const counter = createCounter(10)
console.log(counter()) // 10
console.log(counter())  // 11
console.log(counter())  // 12
 // each time the fucntion is called it is passed the prior as a stored hiddin value