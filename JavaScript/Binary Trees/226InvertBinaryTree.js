var invertTree = function(root) {
    if (!root) return root;
    let left = root.left;
    //root left will equal [2,1,3]
    //root right will equal [7,6,9]
    root.left = invertTree(root.right);
    //root.left will now eqaul [7,9,6]
    root.right = invertTree(left);
    //root.right will now eqaul [2,3,1]
    return root;
    //root now equals [4,7,2,9,6,3,1]

};


console.log(invertTree([4,2,7,1,3,6,9]))