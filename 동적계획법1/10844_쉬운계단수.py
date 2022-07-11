# 쉬운 계단 수

# 45656 인접한 모든 자리의 차이가 1
# 0을 제외한 모든 숫자는 앞에 올수 있다
# 1~8은 뒤에 올 수 있는 숫자가 2종류
# 9뒤엔 8만이 올 수 있다.
#            0  1  2  3  4  5  6  7  8  9
# 자리수(1)   0  1  1  1  1  1  1  1  1  1
# 자리수(2)   1  1  2  2  2  2  2  2  2  1
# 자리수(3)   1  3  3  4  4  4  4  4  3  2
# dp[i]는 대각선 왼쪽위, 오른쪽 위의 합

import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % MOD)