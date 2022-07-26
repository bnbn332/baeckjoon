# 스택 수열

import sys
input = sys.stdin.readline

count = 1
temp = True
stack = []
op = []

n = int(input())

for i in range(n):
    num = int(input())
    # num 이하 숫자까지 스택에
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없을때
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for i in op:
        print(i)

