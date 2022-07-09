# 링

import sys
input = sys.stdin.readline

# 링의 개수 N
n = int(input())
# 링의 반지름(바닥에 놓은 순서)
radius = list(map(int, input().split()))

result = []


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


for i in range(1, len(radius)):
    radius_first = radius[0]
    radius_next = radius[i]

    up = radius_first / gcd(radius_first, radius_next)
    down = radius_next / gcd(radius_first, radius_next)
    print(str(int(up)) + '/' + str(int(down)))