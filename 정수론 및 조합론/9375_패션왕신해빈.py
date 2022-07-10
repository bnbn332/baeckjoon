# 패션왕 신해빈
# 종류별 옷의 수 + 1 을 전부 곱하고 알몸의 경우의 수인 1을 뺀다

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    clothes = {}

    # 의상의 개수 n
    n = int(input())
    for _ in range(n):
        name, type = input().split()
        print(clothes.keys())
        # 의상 종류를 dict의 key로 사용
        if(type in clothes):
            clothes[type] += 1
        else:
            clothes[type] = 1

    case = 1
    for key in clothes.keys():
        case = case * (clothes[key] + 1)

    print(case - 1)