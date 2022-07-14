# 인간-컴퓨터 상호작용

import sys
input = sys.stdin.readline

s = input()
# 질문의 수 q
q = int(input())

for _ in range(q):
    question = input().split()
    sum = 0
    for i in range(int(question[1]), int(question[2]) + 1):
        if s[i] == question[0]:
            sum += 1
    print(sum)