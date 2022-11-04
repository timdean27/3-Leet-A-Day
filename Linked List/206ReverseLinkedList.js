// Given the head of a singly linked list, reverse the list, and return the reversed list.

// Example 1:


// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]
// Example 2:


// Input: head = [1,2]
// Output: [2,1]

class Node {
    constuctor(value,next){
        this.value = value;
        this.next = next ? next :null
    }

}

const initializeLinkedListFromArray = array =>{
    if(array.length === 0){
        return [];
    }
    let head = new Node(array[0])
    let current = head;

    for(let i = 1; i < array.length; i++){
        let newNode = new Node(array[i]);
        current.next = newNode;
        current = current.next
    }
    return  head;
}


const printLinkedList = head =>{
    let current = head;
    let printStr = "";
    while(current){
        printStr += current.value + "->";
        current = current.next
    }

    console.log(printStr)
}





var reverseList = function(head) {
    let previous = null
    let current = head
    // console.log(head)
while(current){
    let nxt = current.next
    // first time around this is set to 2
    // second time this is set to 3
    current.next = previous
    //first time this is set to null
    //second time this is set to 1
    previous= current
    //first time this is set to 1
        //meaning current.next is of previous is null
    //second time this is seet to 2
        //meaning current.next is of previous is 1
    //this means the chain is no 2->1
    current = nxt
    //first time this is now set to 2
    //second time this is set to 3
    
}
return previous
};

console.log(reverseList(initializeLinkedListFromArray([1,2,3,4,5])))