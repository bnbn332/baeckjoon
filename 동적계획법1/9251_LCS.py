# LCS 2차원 배열을 사용

import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

h = len(s1)
w = len(s2)

dp = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp[-1][-1])