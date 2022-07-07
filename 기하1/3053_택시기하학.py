# 택시 기하학

# D(T1, T2) = |X1 - X2| + |Y1 - Y2|
import math
import sys
input = sys.stdin.readline

r = int(input())
answer1 = f'{r * r * math.pi: .6f}'
answer2 = f'{2 * r * r: .6f}'

print(answer1)
print(answer2)

