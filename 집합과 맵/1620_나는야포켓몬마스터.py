# 나는야 포켓몬 마스터
import sys

n, m = map(int, input().split())    # 도감에 수록되어 있는 포켓몬 수 N, 맞춰야 하는 문제의 개수 M

pocketmon_int_key = {}
pocketmon_name_key = {}

for i in range(n):                                               # pocketmon_int_key = {0: 'a', 1: 'b', 2: 'c'}
    name = sys.stdin.readline().strip()                          # pocketmon_name_key = {'a': 0, 'b': 1, 'c': 2}
    pocketmon_int_key[i] = name
    pocketmon_name_key[name] = i

for _ in range(m):
    item = sys.stdin.readline().strip()
    if item.isdigit() == True:  # 입력값이 int인 경우
        print(pocketmon_int_key[int(item) - 1])
    else:
        print(pocketmon_name_key[item] + 1)
