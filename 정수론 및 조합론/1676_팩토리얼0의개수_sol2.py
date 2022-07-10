# 팩토리얼 0의 개수
# n에서 5로 나눠 떨어지는 수가 몇개인지 구한다

import sys
input = sys.stdin.readline

n = int(input())
count = 0

# n이 5이상이면 while문을 돌려
while n >= 5:
    # 5로 나눈 몫은 0의 개수가 되고,
    count += n // 5

    # 5가 2번있는 것은 2개 증가를 위해
    n //= 5

print(count)