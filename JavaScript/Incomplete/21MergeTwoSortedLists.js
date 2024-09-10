// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.

 

// Example 1:


// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1,1,2,3,4,4]
// Example 2:

// Input: list1 = [], list2 = []
// Output: []
// Example 3:

// Input: list1 = [], list2 = [0]
// Output: [0]


var mergeTwoLists = function(list1, list2) {
    if (!list1[0]) return list2;
    if (!list2[0]) return list1;
    for(let i = 0; i < list1.length; i++) {
        console.log(list1[i])
        if(list1[i] == list2[i] ){
            list1.splice(i,0,list2[i])
        }
        else if(list1[i] < list2[i]){
            list1.splice(i,0,list2[i])
        }
    }
    list1.sort((a,b)=> a - b)
    return list1
};

console.log(mergeTwoLists([1,2,4],[1,3,4]));

console.log(mergeTwoLists([],[]));
console.log(mergeTwoLists([],[0]));