# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array with amount + 1, which is an impossible value
        dp = [float('inf')] * (amount + 1)
        print(dp)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0

        # Iterate over each coin
        for a in range(1, amount + 1):
            for i in range(len(coins)):
                if a - coins[i] >= 0:
                    # if current amount is >=0 we find the min
                    print(dp[a])
                    dp[a] = min(dp[a], 1 + dp[a - coins[i]])
                    print(dp)
        # If dp[amount] is still amount + 1, then it's not possible to make that amount
        return dp[amount] if dp[amount] != amount + 1 else -1


sol = Solution()
print(sol.coinChange(coins = [1,3,4,5], amount = 7))


# first iteration
#  a = 1  
# first coin = 1
# a - coin = 1-1 = 0 
# dp[1] = min(inf, 1+[dp[a-coin]])  dp[a-coin] = dp[0] = 0
# dp[1] = 1 + 0 = 1

# second iteration
#  a = 2  
# first coin = 1
# a - coin = 2-1 = 1 
# dp[2] = min(inf, 1+[dp[a-coin]])  dp[a-coin] = dp[1] = 1
# dp[2] = 1 +1 = 2

# third iteration
#  a = 3
# first coin = 1
# a - coin = 3-1 = 2 
# dp[3] = min(inf, 1+[dp[a-coin]])  dp[a-coin] = dp[2] = 2
# dp[3] = 1 +2 = 3

# second coin = 3
# a - coin2 = 3 - 3 = 0
# dp[3] = min(3 , 1+[dp[a-coin]])  dp[a-coin] = dp[0] = 0
# dp[3] = 1+ 0 = 1


# fourth iteration
#  a = 4
# first coin = 1
# a - coin = 4-1 = 3 
# dp[4] = min(inf, 1+[dp[a-coin]])  dp[a-coin] = dp[3] = 1
# dp[4] = 1 + 1 = 2

# second coin = 3
# a - coin2 = 4 - 3 = 1
# dp[4] = min(2 , 1+[dp[a-coin]])  dp[a-coin] = dp[1] = 0
# dp[3] = 1+ 1 = 2

# third coin = 4
# a - coin3 = 4 - 3 = 1
# dp[4] = min(2 , 1+[dp[a-coin3]])  dp[a-coin3] = dp[0] = 0
# dp[4] = 1+ 0 = 1

# we get dp[4] = 1



# fith iteration
#  a = 5
# first coin = 1
# a - coin = 5-1 = 4 
# dp[5] = min(inf, 1+[dp[a-coin]])  dp[a-coin] = dp[4] = 1
# dp[5] = 1 + 1 = 2

# second coin = 3
# a - coin2 = 5 - 3 = 2
# dp[5] = min(2 , 1+[dp[a-coin2]])  dp[a-coin2] = dp[2] = 2
# dp[3] = min(2 , 1+2) = 2

# third coin = 4
# a - coin3 = 5 - 4 = 1
# dp[5] = min(2 , 1+[dp[a-coin3]])  dp[a-coin3] = dp[1] = 1
# dp[5] = min(2,1+1) = 2

# fourth coin = 5
# a - coin3 = 5 - 5 = 0
# dp[5] = min(2 , 1+[dp[a-coin3]])  dp[a-coin3] = dp[0] = 0
# dp[5] = min(2,1+0) = 1

# we get dp[5] = 1



# sixth iteration
#  a = 6
# first coin = 1
# a - coin = 6-1 = 5 
# dp[6] = min(inf, 1+[dp[a-coin]])  dp[a-coin] = dp[5] = 1
# dp[6] = 1 + 1 = 2

# second coin = 3
# a - coin2 = 6 - 3 = 3
# dp[6] = min(2 , 1+[dp[a-coin2]])  dp[a-coin2] = dp[3] = 1
# dp[3] = min(2 , 1+1) = 2

# third coin = 4
# a - coin3 = 6 - 4 = 2
# dp[6] = min(2 , 1+[dp[a-coin3]])  dp[a-coin3] = dp[2] = 2
# dp[6] = min(2,1+2) = 2

# fourth coin = 5
# a - coin3 = 6 - 5 = 1
# dp[6] = min(2 , 1+[dp[a-coin3]])  dp[a-coin3] = dp[1] = 1
# dp[6] = min(2,1+1) = 2

# we get dp[6] = 2


# seventh iteration
#  a = 7
# first coin = 1
# a - coin = 7-1 = 6 
# dp[6] = min(inf, 1+[dp[a-coin]])  dp[a-coin] = dp[6] = 2
# dp[6] = 1 + 1 = 3

# second coin = 3
# a - coin2 = 7 - 3 = 4
# dp[7] = min(3 , 1+[dp[a-coin2]])  dp[a-coin2] = dp[4] = 1
# dp[3] = min(2 , 1+1) = 2

# third coin = 4
# a - coin3 = 7 - 4 = 3
# dp[7] = min(2 , 1+[dp[a-coin3]])  dp[a-coin3] = dp[3] = 1
# dp[7] = min(2,1+1) = 2

# fourth coin = 5
# a - coin3 = 7 - 5 = 2
# dp[7] = min(2 , 1+[dp[a-coin3]])  dp[a-coin3] = dp[2] = 2
# dp[7] = min(2,1+2) = 2

# we get dp[7] = 2