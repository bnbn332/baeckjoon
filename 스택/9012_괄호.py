# 괄호

import sys
input = sys.stdin.readline

# 테스트 케이스 T
t = int(input())

for _ in range(t):
    data = input()
    data_list = list(data)  # list()써서 문자열 자르기
    sum = 0

    for i in data_list:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        # ')' 로 시작 하는 경우
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')