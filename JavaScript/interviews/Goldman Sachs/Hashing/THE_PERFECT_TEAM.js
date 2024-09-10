// The Perfect Team

function perfectTeam(skills) {
    let splitskill = skills.split("").sort();
    // console.log(splitskill)
    let hash = {}
    let result = Infinity
    for(let i = 0; i < splitskill.length; i++) {
        if(hash[splitskill[i]]){
            hash[splitskill[i]].push(splitskill[i])
          }
          else{
            hash[splitskill[i]] =[splitskill[i]]
          }
    }
    const keys = Object.keys(hash);
    // console.log(keys.length)
    const values = Object.values(hash);
    console.log(values[0])
     if(keys.length == 5){
        for(let i = 0; i < values.length; i++){
            if(values[i].length < result){
                result = values[i].length
                
            }
        }
     }
     else{ result = 0}
     return result
}

console.log(perfectTeam('bbbbcccmmmmmppppzzzzz'))
console.log(perfectTeam('pcmpp'))