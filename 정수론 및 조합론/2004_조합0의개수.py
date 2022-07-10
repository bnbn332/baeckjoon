# 조합 0의 개수

# 팩토리얼로 구할시 시간초과
# 끝자리가 0이면 10의 배수
# 10은 2와 5로 이루어짐
# 짝이 맞아야 함으로 더 작은 개수가 10의 개수

import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


five_count = count_number(n, 5) - count_number(m, 5) - count_number(n - m, 5)
two_count = count_number(n, 2) - count_number(m, 2) - count_number(n - m, 2)

answer = min(five_count, two_count)
print(answer)