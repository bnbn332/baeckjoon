# 포도주 시식

# dp[i]는 i번째 포도주까지 최대로 마신 포도주의 양
# 이전 와인잔을 마신 경우 = array[i] + array[i - 1] + dp[i - 3]
# 이전 와인잔을 마시지 않은 경우 = array[i] + dp[i - 2]
# 현재 와인잔을 마시지 않은 경우 = dp[i - 1]

import sys
input = sys.stdin.readline

n = int(input())
array = [0] * 10000
for i in range(n):
    array[i] = int(input())

dp = [0] * 10000
dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[2] + array[0], array[2] + array[1], dp[1])
for i in range(3, n):
    dp[i] = max(array[i] + array[i - 1] + dp[i - 3], array[i] + dp[i - 2], dp[i - 1])

print(max(dp))