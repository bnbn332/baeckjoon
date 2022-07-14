# 동전 0

import sys
input = sys.stdin.readline

# 동전의 가치n, k = target_number
n, k = map(int, input().split())

coin_value = []
for _ in range(n):
    coin_value.append(int(input()))

count = 0
coin_value.sort(reverse=True)

for i in range(n):
    count += k // coin_value[i]
    k = k % coin_value[i]

print(count)