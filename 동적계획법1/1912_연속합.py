# 연속합
# 연속된 수를 선택해서 구할 수 있는 합 중 가장 큰수
# dp[i] = max(arr[i], dp[i - 1] + arr[i])

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
dp = [0 for _ in range(len(arr))]
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))