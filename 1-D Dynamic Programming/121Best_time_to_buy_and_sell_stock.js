// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

// Example 1:

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
// Example 2:

// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transactions are done and the max profit = 0.


var maxProfit = function(prices) {
    let lowest = prices[0]
    let maxProfit = 0
    for(let i = 0; i < prices.length; i++) {
        lowest = Math.min(lowest, prices[i])
        console.log("lowest", lowest)
        //Can not go back days and get lower so once maxProfit is set it doesnt matter if price drops
        //as long as Maxprofit isnt greater
        maxProfit = Math.max(maxProfit, prices[i] - lowest)
        console.log("maxProfit", maxProfit)
    }

    return (maxProfit)
};

console.log(maxProfit([7,2,8,1,6,4]))
// console.log(maxProfit([7,6,4,3,1]))
// console.log(maxProfit([2,4,1]))
// console.log(maxProfit([7,6,4,3,1]))
// console.log(maxProfit([3,2,6,5,0,3]))