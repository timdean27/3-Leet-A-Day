var mergeTwoLists = function(list1, list2) {
    let length = 0
    let newArray =[]
    if(list1.length > list2.length){
        length = list1.length
    }
    else{ length = list2.length}
    console.log(length)


    for(let x = 0; x < length; x++){
        let BigInt = 0
        if (list1[x] == null && list2[x] != null){
            newArray.push(list2[x])
        }
        else if (list1[x] != null && list2[x] == null){
            newArray.push(list1[x])
        }
        else if(list1[x] == list2[x]){
            newArray.push(list1[x],list2[x])
        }
        else if (list1[x] > list2[x]){
            newArray.push(list2[x])
            BigInt = list1[x]
        }
        else if (list1[x] < list2[x]){
            newArray.push(list1[x])
            BigInt = list2[x]
        }
        
        if(BigInt > 0){
        newArray.push(BigInt)
        }
    }
    return newArray;
};

console.log(mergeTwoLists([1,2,4],[1,3,4]))
console.log(mergeTwoLists([],[0]))
console.log(mergeTwoLists([],[]))