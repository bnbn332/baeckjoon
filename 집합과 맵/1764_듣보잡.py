# 듣보잡 (set이용)
from sys import stdin

n, m = map(int, input().split())     # 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M

listen = set()
for _ in range(n):
    listen.add(stdin.readline().strip())

see = set()
for _ in range(m):
    see.add(stdin.readline().strip())

answer = sorted(list(listen & see))

print(len(answer))
for i in answer:
    print(i)