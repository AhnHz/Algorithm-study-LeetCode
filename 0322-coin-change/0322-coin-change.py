class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        if amount == 0:
            return dp[0]

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)    

        return dp[amount] if dp[amount] != float('inf') else -1
                