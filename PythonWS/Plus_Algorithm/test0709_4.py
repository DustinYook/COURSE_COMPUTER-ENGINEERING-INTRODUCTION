# 프로그램 목적: 정렬 알고리즘 구현 (선택, 버블, 삽입)


def selection_sort(li):  # 선택정렬
    print(li)
    for i in range(0, len(li)):  # 칸막이 처럼 생각
        print(li)
        for j in range(i, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]  # 파이썬에서는 swap 안써도 됨
    print(li)
    return li


def bubble_sort1(li):  # 버블정렬 -> 내림차순
    for i in range(0, len(li) - 1):
        print(li)
        for j in range(i + 1, len(li)):
            if li[j] > li[j - 1]:
                li[j], li[j - 1] = li[j - 1], li[j]
    return li


def bubble_sort2(li):  # 버블정렬 -> 오름차순
    for i in range(0, len(li)-1):
        for j in range(len(li)-1, i, -1):
            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]
                print(li)
    return li


def insertion_sort(li):  # 삽입정렬
    print(li)
    for i in range(1, len(li)):   # 0번부터가 아닌 1번부터!
        print(li)
        for j in range(i, 0, -1):  # 인덱스 가장 앞까지 진행
            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]
            else:
                break  # 삽입정렬의 자이
    print(li)
    return li

lists = [23, 78, 45, 8, 32, 56]
print('선택정렬:', selection_sort(lists))
print('버블정렬1:', bubble_sort1(lists))
print('버블정렬2:', bubble_sort2(lists))
print('삽입정렬:', insertion_sort(lists))