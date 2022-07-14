# ATM

import sys
input = sys.stdin.readline

# 사람의 수 N
n = int(input())
# 각 사람이 돈을 인출 하는데 걸리는 시간
time = list(map(int, input().split()))
time.sort()

for i in range(1, n):
    time[i] += time[i - 1]

print(sum(time))