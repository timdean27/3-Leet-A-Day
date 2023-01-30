var addTwoNumbers = function(l1, l2) {
    let array = []
    let array2 = []
    let z = 0
    let y = 0
    for(let i = 0; i < l1.length; i++){
        array.push(l1[(l1.length-1)-i])    
        z++
    }
    for(let i = 0; i < l2.length; i++){
        array2.push(l2[(l2.length-1)-i])    
        y++
    }
    console.log(array , array2, z , y)
   
};




console.log(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))