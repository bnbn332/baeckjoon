# 다리 놓기(조합)

import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


t = int(input())

for _ in range(t):
    # 서쪽, 동쪽 사이트 개수 N, M
    n, m = map(int, input().split())
    # nCr = n! // (n - r)! * r!
    answer = factorial(m) // (factorial(m - n) * factorial(n))

    print(answer)