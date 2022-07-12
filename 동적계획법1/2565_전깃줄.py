# 전깃줄

import sys
input = sys.stdin.readline

n = int(input())

line = []

for _ in range(n):
    line.append(list(map(int, input().split())))

line.sort() # A전봇대 기준 정렬

dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))