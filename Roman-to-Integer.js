//PASS

var romanToInt = function(s) {
    var map = {
        I: 1,
        IV: 4,
        V: 5,
        IX: 9,
        X: 10,
        XL: 40,
        L: 50,
        XC: 90,
        C: 100,
        CD: 400,
        D: 500,
        CM: 900,
        M: 1000
      };
    let sum = 0
    //console.log(typeof(sum))
    for (let i = 0; i < s.length; i++) {
        //console.log(s.substr(i, 2))
      if(map[s.substr(i, 2)]) {
        sum += map[s.substr(i, 2)];
            i++
      } else {
        sum += map[s[i]];
 
      }
    }

    return sum
};


console.log(romanToInt("MCMXCIV"));
console.log(romanToInt("LVIII"));
console.log(romanToInt("III"));