# 검문

# A = M * a + R
# B = M * b + R
# C = M * c + R

# A - B = M(a - b)
# B - C = M(b - c)

# M은 A - B, B - C 의 공약수
# 최대 공약수를 구한 후 1을 제외한 약수 출력

from math import sqrt
import sys
input = sys.stdin.readline


# 최대 공약수 함수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 종이에 적은 수에 개수 N
n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

answer = []
result = []
for i in range(1, n):
    result.append(numbers[i] - numbers[i - 1])

prev = result[0]
for i in range(1, len(result)):
    prev = gcd(prev, result[i])

for i in range(2, int(sqrt(prev)) + 1):  # 제곱근까지만 탐색
    if prev % i == 0:
        answer.append(i)
        answer.append(prev // i)
answer.append(prev)
answer = list(set(answer))  # 중복 제거
answer.sort()
print(*answer)