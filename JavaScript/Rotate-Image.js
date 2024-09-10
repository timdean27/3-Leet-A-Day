var rotate = function(matrix) {
    let x =[]
    let y = [[]]
    let z = []
    for (let i = 0; i < matrix.length; i++){
        x = matrix[(matrix.length-1)-i]
        console.log("x",x)
        for (let j = 0;j < x.length; j++){
           y[i][i]= x[j]
           console.log("y",y)
        }
    }
   
};

rotate([[1,2,3],[4,5,6],[7,8,9]])
//console.log(rotate([[1,2,3],[4,5,6],[7,8,9]]))
//console.log(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))