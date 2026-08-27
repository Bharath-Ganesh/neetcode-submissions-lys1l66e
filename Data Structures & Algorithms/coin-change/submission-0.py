class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = [1,5,10], amount = 12
        """
         0  1   2   3   4   5   6   7  8    9  10   11 12         
        [0  1   2   3   4   1 inf inf inf inf inf inf inf]
        """
        INF   = float('inf')
        dp    = [INF] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        return -1 if dp[amount] == INF else dp[amount]


        