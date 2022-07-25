# 주유소

import sys
input = sys.stdin.readline

# 도시의 개수 N
n = int(input())

# 도로의 길이 리스트
road_length = list(map(int, input().split()))

# 주유소 리터당 가격
oil_price = list(map(int, input().split()))

min_price = oil_price[0]
sum = 0

for i in range(n - 1):
    if min_price > oil_price[i]:
        min_price = oil_price[i]
    sum += (min_price * road_length[i])

print(sum)
