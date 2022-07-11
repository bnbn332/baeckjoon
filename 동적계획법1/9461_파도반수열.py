# 파도반 수열

import sys
input = sys.stdin.readline

# 1 1 1 2 2 3 4 5 7 9
dp = [0 for _ in range(101)]

dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(4, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
