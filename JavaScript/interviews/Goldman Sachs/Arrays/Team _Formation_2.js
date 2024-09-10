// FC cod


function countTeams(skills, minPlayers, minLevel, maxLevel) {

let filtered = []
let unique = []
let last = Infinity
let result = 0
// let result = {}
   for(let i =0; i <skills.length ; i ++ ){
       if(skills[i]>=minLevel && skills[i]<= maxLevel){
           filtered.push(skills[i])
       }
   }
//    console.log(filtered)
    filtered.sort((a, b)=> a - b)
    // console.log(filtered)
   for(let j = 0; j < filtered.length; j++){
        if(filtered[j] != last){
            unique.push(filtered[j])
            
        }
        last = filtered[j]
    }
    // console.log(unique)
  
  
    //combinations = unique!/(unquie-minPlayers!)(minPlayers!)
    // 4*3*2*1 /(1)(3*2*1) = 4
    //4*3*2*1 /(1)(4*3*2*1) = 1
    //result = 5

    function product(a,b) {
      let mult = a
      let i = a;
      while (i++< b) {
        mult*=i;
      }
      return mult;
    }
    function combo(groupSize, limit) 
    {
      if (groupSize==limit || limit==0) { return 1;} 
      else 
      {
        return product(limit+1, groupSize)/product(1,groupSize-limit);
      }
    }
      for(let k = unique.length; k >= minPlayers; k--){
        // console.log(k,"k")
        // console.log(combo(unique.length, k));
        result = (combo(unique.length, k)) + result;
    }
    return result
}

console.log(countTeams([12,4,6,13,5,5,10],3,4,10))