# 회의실 배정

import sys
input = sys.stdin.readline

# 회의의 수 N
n = int(input())

time = []
for _ in range(n):
    start, end = list(map(int, input().split()))
    time.append((start, end))

time = sorted(time, key=lambda a: a[0]) # 시작 시간 기준 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간 기준 오름차순

last = 0    # 회의 마지막 시간
count = 0    # 회의 개수

for i, j in time:
    if i >= last:   # 시작 시간이 회의의 마지막 시간보다 크거나 같을경우
        count += 1
        last = j

print(count)