# 스택

import sys
input = sys.stdin.readline

# 명령의 수 N
n = int(input())

stack = []
for _ in range(n):
    commands = input().split()
    order = commands[0]

    if order == 'push':
        value = commands[1]
        stack.append(value)

    elif order == 'pop':
        # 스택이 비어있을 경우
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
