
function ReverseString(str){
 const strToArry = str.split("")
 strToArry.reverse()
 return strToArry.join('')
}

console.log(ReverseString("CodingMoney"))