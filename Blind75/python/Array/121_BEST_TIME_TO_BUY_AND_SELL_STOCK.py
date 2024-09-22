# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_min_price_index = 0
        max_profit = 0 
        for i in range(1, len(prices)):
            # find the lowest price , this does not mean that max profit will alwaays start with the lowest price
            # this part just find the lowest price next checks if we find a larger max profit with this new lower price
            # but if we hit a lower price in series that means we either should have already sold , or this is new best time to buy
            if prices[current_min_price_index] > prices[i]:
                current_min_price_index = i

            # once we have set the current low we check the profit from currnet price - current low
            # if this is larger than a prior found max profit we set this to new max profit
            if prices[i] - prices[current_min_price_index] > max_profit:
                max_profit = prices[i] - prices[current_min_price_index]

            # curMin = prices[0]
            # max_profit = 0 
            # for i in range(len(prices)):
                # curMin = min(prices[i], curMin)
                # max_profit = max(max_profit, prices[i]- curMin)

        return max_profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))