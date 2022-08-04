const items = [
    { name: 'Bike', price: 100 },
    { name: 'TV', price: 200 },
    { name: 'Album', price: 10 },
    { name: 'Book', price: 5 },
    { name: 'Phone', price: 500 },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25 },
]
//filter
const filteredItems = items.filter((item)=>{
    return item.price <= 100
})
console.log(filteredItems)

//map
const itemNames = items.map((item)=>{
    return item.name 
})
console.log(itemNames)

//find
const foundItem = items.find((item)=>{
    return item.name === 'Book'
})
console.log(foundItem)

//for each
items.forEach((item)=>{
    console.log(item.name)
})

//some
const  hasInexpensiveItems = items.some((item)=>{
    return item.price <= 100
})
console.log(hasInexpensiveItems)

//every // checks if all items work if not return false
const  everyInexpensiveItems = items.every((item)=>{
    return item.price <= 100
})
console.log(everyInexpensiveItems)

//reduce

const  total = items.reduce((currentTotal, item) =>{
    return item.price + currentTotal
}, 0)
//starting at 0 or listed start, itterate and sum
console.log(total)

const nums = [1,2,3,4,5,6]
 const includesNum = nums.includes(2)
 console.log(includesNum)
