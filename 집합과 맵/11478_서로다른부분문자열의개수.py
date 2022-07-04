# 서로 다른 부분 문자열의 개수

from sys import stdin

s = stdin.readline().strip()
answer = set()              # 부분 문자열을 저장할 set

for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i: j+1]
        answer.add(temp)
        print(answer)
print(len(answer))