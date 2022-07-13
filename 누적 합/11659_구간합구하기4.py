# 구간 합 구하기 4

import sys
input = sys.stdin.readline

# 수의 개수 N, 구해야 하는 횟수 M
n, m = map(int, input().split())

numbers = list(map(int, input().split()))
prefix_sum = [0]

temp = 0
for i in numbers:
    temp += i
    prefix_sum.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])