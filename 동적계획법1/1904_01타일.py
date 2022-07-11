# 01 타일

# n = 1 -> 1
# n = 2 -> 00 11
# n = 3 -> 111 100 001
# d[i] = d[n-1] +d[n-2]

import sys
input = sys.stdin.readline

dp = [0 for _ in range(1000001)]

n = int(input())
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
print(dp[n])