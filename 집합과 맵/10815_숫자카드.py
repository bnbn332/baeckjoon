# 숫자 카드(set 써서)

n = int(input())                        # 상근이 카드 개수
cards = set(map(int, input().split()))  # 상근이 카드 목록

m = int(input())                        # 비교할 카드 개수
cards_compare = list(map(int, input().split()))  # 비교할 카드 목록


for i in cards_compare:
    if i in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")
