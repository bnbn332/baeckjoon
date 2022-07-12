# 가장 긴 바이토닉 부분 수열

# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면 바이토닉 수열
# 증가하는 수열 길이 + 감소하는 수열 길이의 합이 가장 큰 지점이 바이토닉 수열의 Sk원소가 된다
#             수열: 1, 5, 2, 1, 4, 3, 4, 5, 2, 1
# 증가하는 수열 길이: 1, 2, 2, 1, 3, 3, 4, 5, 2, 1
# 감소하는 수열 길이: 1, 5, 2, 1, 4, 3, 3, 3, 2, 1
#          길이 합: 2, 7, 4, 2, 7, 6, 7, 8, 4, 2
#            결과:  1, 6, 3, 1, 6, 5, 6, 7, 3, 1

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

increase = [0 for _ in range(n)]
decrease = [0 for _ in range(n)]
mix = [0 for _ in range(n)]


for i in range(n):
    for j in range(i):
        if a[i] > a[j] and increase[i] < increase[j]:
            increase[i] = increase[j]
    increase[i] += 1

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and decrease[i] < decrease[j]:
            decrease[i] = decrease[j]
    decrease[i] += 1

for i in range(n):
    mix[i] = increase[i] + decrease[i] -1
print(max(mix))