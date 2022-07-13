# 평범한 배낭 냅색 알고리즘

import sys
input = sys.stdin.readline

# 물품의 수 N, 준서가 버틸 수 있는 무게 K
n, k = map(int, input().split())

item = [[0, 0]]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    # 물건의 무게 W, 물건의 가치 V
    w, v = map(int, input().split())
    item.append((w, v))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = item[i][0]
        value = item[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])