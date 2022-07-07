# 약수

import sys
input = sys.stdin.readline

# 진짜 약수의 개수
divisor_count = int(input())

divisors = list(map(int, input().split()))

# 가장 큰 수
max_divisor = max(divisors)
# 가장 작은 수
min_divisor = min(divisors)
print(max_divisor * min_divisor)