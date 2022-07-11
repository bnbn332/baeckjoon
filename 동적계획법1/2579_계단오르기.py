# 계단오르기

import sys
input = sys.stdin.readline

n = int(input())

array = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(n):
    array[i] = int(input())

dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[2] + array[1], array[2] + array[0])

for i in range(3, n):
    dp[i] = max(array[i] + array[i - 1] + dp[i - 3], array[i] + dp[i - 2])

print(dp[n - 1])