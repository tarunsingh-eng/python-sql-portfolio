def coinChange(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0]=0
    for n in range (amount+1):
        for c in coins:
            if n - c >= 0:
                dp[n] = min(dp[n], 1 + dp[n-c])
    return dp[amount] if dp[amount] != amount + 1 else - 1


print(coinChange([1,2,5,10,50,100,500,1000],898))