
#Coin Change: https://leetcode.com/problems/coin-change-ii/description/
#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
#
#Input: amount = 5, coins = [1,2,5]
#Output: 4
#Explanation: there are four ways to make up the amount:
#5=5
#5=2+2+1
#5=2+1+1+1
#5=1+1+1+1+1
#
#

def change(amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]* (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]


"""
amount 5, coins [1, 2, 5]
dp = [0,0,0,0,0,0]
dp = [1,0,0,0,0,0]
for coin in coins: 3
for x in 1, 6
    dp[1] = dp[0]

dp = [1,1,1,1,1,1]

coin 2
de 2 a 6
dp[1,1,2, 2, 3, 3 ]
coin 5
de 5 a 6
dp[1,1,2,2, 4, 3]
dp[amount] = 4
"""