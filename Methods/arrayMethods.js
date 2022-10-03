const items = [
    { name: 'Bike', price: 100 },
    { name: 'TV', price: 200 },
    { name: 'Album', price: 10 },
    { name: 'Book', price: 5 },
    { name: 'Phone', price: 500 },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25 },
]

// sort
let nums1 = [0,3,5,4,7,2,1]
nums1.sort((a, b)=> a - b)
console.log(nums1)
// [ 0, 1, 2, 3, 4, 5, 7]

//filter
const filteredItems = items.filter((item)=>{
    return item.price <= 100
})
console.log(filteredItems)
// [
//     { name: 'Bike', price: 100 },
//     { name: 'Album', price: 10 },
//     { name: 'Book', price: 5 },
//     { name: 'Keyboard', price: 25 }
//   ]


//map
const itemNames = items.map((item)=>{
    return item.name 
})
console.log(itemNames)
// [
//     'Bike',     'TV',
//     'Album',    'Book',
//     'Phone',    'Computer',
//     'Keyboard'
//   ]


//find
const foundItem = items.find((item)=>{
    return item.name === 'Book'
})
console.log(foundItem)
// { name: 'Book', price: 5 }


//for each
items.forEach((item)=>{
    console.log(item.name)
})
// Bike
// TV
// Album
// Book
// Phone
// Computer
// Keyboard


//some
const  hasInexpensiveItems = items.some((item)=>{
    return item.price <= 100
})
console.log(hasInexpensiveItems)
// true


//every // checks if all items work if not return false
const  everyInexpensiveItems = items.every((item)=>{
    return item.price <= 100
})
console.log(everyInexpensiveItems)
// false


//reduce
const  total = items.reduce((currentTotal, item) =>{
    return item.price + currentTotal
}, 0)
//starting at 0 or listed start, iterate and sum
console.log(total)
// 1840

//includes
const nums = [1,2,3,4,5,6]
 const includesNum = nums.includes(2)
 console.log(includesNum)
//  true


//tostring
const numsString = [1,2,3,4,5,6]
console.log(numsString.toString())
// 1,2,3,4,5,6
console.log(numsString.toString().split(""))
// [
//     '1', ',', '2', ',',
//     '3', ',', '4', ',',
//     '5', ',', '6'
//   ]