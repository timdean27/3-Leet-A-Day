// Write a function createCounter. 
// It should accept an initial integer init. 
// It should return an object with three functions.

// The three functions are:

// increment() increases the current value by 1 
// and then returns it.
// decrement() reduces the current value by 1 
// and then returns it.
// reset() sets the current value to init and 
// then returns it.
 

// Example 1:

// Input: init = 5, calls = ["increment","reset","decrement"]
// Output: [6,5,4]
// Explanation:
// const counter = createCounter(5);
// counter.increment(); // 6
// counter.reset(); // 5
// counter.decrement(); // 4


function createCounter(init){
    let number = init
    function increment(){
        return ++number
    }
    function decrement(){
        return --number
    }
    function reset(){
        number = init
        return number
    }
    return {
        increment:increment,
        decrement:decrement,
        reset:reset,
    }
}

function counter(init, calls) {
    const counterInstance = createCounter(init);
    return calls.map(call => counterInstance[call]());
}
console.log(counter(init = 5, calls = ["increment","reset","decrement"]))


// with Class and constructor 

class Counter {
    constructor(init){
        this.init = init;
        this.count = init;
    }
    increment(){
        return ++this.count
    }
    decrement(){
        return --this.count
    }
    reset(){
        this.count = this.init
        return this.count
    }
}

// Function to process the calls
function processCalls(init, calls) {
    const counter = new Counter(init);
    const results = [];
    for (const call of calls) {
        results.push(counter[call]());
    }
    return results;
}

// Example usage
const init = 5;
const calls = ["increment", "reset", "decrement"];
const output = processCalls(init, calls);
console.log(output); // Output: [6, 5, 4]