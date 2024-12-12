// Given an integer n, return a counter function. This counter function initially returns n and then returns 1 more than the
// previous value every subsequent time it is called (n, n + 1, n + 2, etc).
// n = 10 
// ["call","call","call"]
// Output: [10,11,12]
// Explanation: 
// counter() = 10 // The first time counter() is called, it returns n.
// counter() = 11 // Returns 1 more than the previous time.
// counter() = 12 // Returns 1 more than the previous time.
var createCounter = function(n) {
    let count = n
    return function() {
        return count++;
    };
};
const counter = createCounter(10); // `count` is initialized to 10

console.log(counter()); // First call:
                        // - Reads `count`: 10
                        // - Increments `count` to 11
                        // - Returns 10

console.log(counter()); // Second call:
                        // - Reads `count`: 11
                        // - Increments `count` to 12
                        // - Returns 11

console.log(counter()); // Third call:
                        // - Reads `count`: 12
                        // - Increments `count` to 13
                        // - Returns 12

//It explains how to write a code and the reason behind writing each line in the code.
