// Given the roots of two binary trees p and q, write a function to check if they are the same or not.

// Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

// Example 1:


// Input: p = [1,2,3], q = [1,2,3]
// Output: true


const isSameTree = (p, q) =>{
    if(p == null && q == null) return true;
    if(p == null || q == null) return false;

    if(p.val === q.val){
        return isSameTree(p.left ,q.left ) && isSameTree(p.right ,q.right)
    }
    return false
}

console.log(isSameTree([1,2,3], [1,2,3]))