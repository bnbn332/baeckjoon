# 배수와 약수

import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    # 첫 번째 숫자가 두 번째 숫자의 약수인 경우
    if b % a == 0:
        print("factor")
    # 첫 번째 숫자가 두 번째 숫자의 배수인 경우
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")