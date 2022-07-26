# 균형잡힌 세상

import sys

input = sys.stdin.readline

while True:
    words = input().rstrip()
    stack = []

    # 종료 조건
    if words == '.':
        break
    true_flag = True

    for i in words:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':  # 스택이 비었거나 짝이 안맞으면
                true_flag = False
                break
            elif stack[-1] == '(':  # 짝이 맞으면 pop()으로 스택에서 제거
                stack.pop()

        elif i == ']':
            if not stack or stack[-1] == '(':
                true_flag = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if true_flag == True and not stack:
        print('yes')
    else:
        print('no')
