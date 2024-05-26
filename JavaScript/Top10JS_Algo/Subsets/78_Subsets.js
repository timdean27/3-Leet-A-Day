// Given an integer array nums of unique elements, return all possible 
// subsets
//  (the power set).

// The solution set must not contain duplicate subsets. Return the solution in any order.

 

// Example 1:

// Input: nums = [1,2,3]
// Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
function subsets(nums) {
    const result = [];

    function backtrack(start, path) {
        console.log(`Path before push :`, path)
        result.push([...path]);
        console.log(`Result after push:`, result)
        for (let i = start; i < nums.length; i++) {
            path.push(nums[i]);
            console.log(`Path after push :`, path)
            backtrack(i + 1, path);
            path.pop();
            console.log(`Path after pop:`, path)
        }
    }

    backtrack(0, []);
    return result;
}


console.log(subsets([1,2,3]))