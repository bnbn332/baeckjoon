# 나머지 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

prefix = [0 for _ in range(m)]
pre_sum = 0

prefix[0] = 1

for i in range(n):
    pre_sum += numbers[i]
    prefix[pre_sum % m] += 1

answer = 0
for i in prefix:
    answer += i * (i - 1) // 2

print(answer)

