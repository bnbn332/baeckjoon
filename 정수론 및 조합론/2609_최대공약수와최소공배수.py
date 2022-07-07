# 최대공약수와 최소공배수

import sys
input = sys.stdin.readline

a, b = map(int, input().split())


# 최대 공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소 공배수
def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))