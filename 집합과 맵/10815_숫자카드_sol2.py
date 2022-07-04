# 숫자카드 (이진 탐색)

n = int(input())    # 상근이 카드 개수
cards = list(map(int, input().split()))
cards.sort()

m = int(input())    # 비교할 카드 개수
cards_compare = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(cards, cards_compare[i], 0, n - 1) is not None:
        print(1, end=" ")
    else:
        print(0, end=" ")