// You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

// Example 1:

// Input: flowerbed = [1,0,0,0,1], n = 1
// Output: true
// Example 2:

// Input: flowerbed = [1,0,0,0,1], n = 2
// Output: false


var canPlaceFlowers = function(flowerbed, n) {
    // we need to plant n flowers
    // can plant a flower when flowerbed[i-1] && flowerbed[i-1] = 0
    let planted = 0
    for(let i = 0; i < flowerbed.length; i++) {

        if(flowerbed[i] == 0 && flowerbed[i-1] !== 1 && flowerbed[i+1] !== 1){
            planted ++
            //if contion is met we skip a i value becasue we are planting a flower
            // [1,0,0,0,0,1] we hit when i = 2 so we skip to i = 3
            i++
        }

        console.log(i)
    }
    // console.log(planted)
    if(planted >= n){return true}
    else {return false}
};

// console.log(canPlaceFlowers([1,0,0,0,1],1))
// console.log(canPlaceFlowers([1,0,0,0,1],2))
// console.log(canPlaceFlowers([1,0,0,0,0,0,1],2))
console.log(canPlaceFlowers([1,0,0,0,0,1],2))
console.log(canPlaceFlowers([0,0,1,0,1],1))