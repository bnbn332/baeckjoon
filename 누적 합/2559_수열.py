# 수열

import sys
input = sys.stdin.readline

# 온도를 측정한 전체 날짜의 수 N, 연속적인 날짜의 수 K
n, k = map(int, input().split())
arr = list(map(int, input().split()))

tmp = sum(arr[:k])
answer = tmp

for i in range(k, n):
    tmp += arr[i] - arr[i - k]
    answer = max(answer, tmp)

print(answer)