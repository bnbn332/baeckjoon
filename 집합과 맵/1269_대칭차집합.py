# 대칭 차집합
from sys import stdin

n, m = map(int, input().split())     # n = A의 원소의개수, m = B의 원소의 개수

a = set(map(int, stdin.readline().split()))
b = set(map(int, stdin.readline().split()))
print(len(a - b) + len(b - a))