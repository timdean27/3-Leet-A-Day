

function ReverseString(num){
    const inToStrin = num.toString();
    console.log(inToStrin);
    
    const strToArry = inToStrin.split("");
    console.log("split", strToArry);
    
    strToArry.reverse();
    console.log("reverse", strToArry);
    
    const reversedStr = strToArry.join('');
    console.log("join", reversedStr);

    return parseInt(reversedStr) * Math.sign(num)
   }
   
   console.log(ReverseString(-15))