//PASS


var lengthOfLastWord = function(s) {
    let array1 = (s.split(" "))
    let array1clean = []
    //console.log("array", array1)
    for (let i = 0; i < array1.length; i++) {
        if(array1[i] != ""){
           array1clean.push(array1[i]) 
        }
    }
    //console.log("array", array1)


    let array2 = array1clean[array1clean.length-1]
    //console.log("array2", array2)
    array3=(array2.split(""))
    //console.log(array3,array3.length)
    return array3.length
};



console.log(lengthOfLastWord("Hello World"))
console.log(lengthOfLastWord("   fly me   to   the moon  "))
console.log(lengthOfLastWord("luffy is still joyboy"))