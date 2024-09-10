function plusMinus(arr) {
    let pos = 0
    let neg = 0
    let zero = 0
 
    for(let i =0; i < arr.length; i ++){
        if(arr[i] > 0){
            pos++
        }
        else if(arr[i] < 0){
            neg++
        }
        else if(arr[i] == 0){
            zero++
        }
    }
let FractionOfPostive = (parseFloat(pos/arr.length).toFixed(6))
let FractionOfNegative = (parseFloat(neg/arr.length).toFixed(6))
let FractionOfZero = (parseFloat(zero/arr.length).toFixed(6))

console.log(FractionOfPostive)
console.log(FractionOfNegative)
console.log(FractionOfZero)
}

plusMinus([1,1,0,-1,-1])