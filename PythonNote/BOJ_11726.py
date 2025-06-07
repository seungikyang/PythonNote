
# BOJ 11726: 2×n 타일링

import sys
input = sys.stdin.readline

MOD = 10_007
n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
    # dp[i] = dp[i-1] + dp[i-2] (mod MOD)   
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= MOD

print(dp[n])