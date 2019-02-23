# 4) 선택정렬 알고리즘 구현하기


def sort(aList):  # 삽입정렬
    for i in range(1, len(aList)):   # 0번부터가 아닌 1번부터!
        for j in range(i, 0, -1):  # 인덱스 가장 앞까지 진행
            if aList[j] < aList[j-1]:
                aList[j], aList[j-1] = aList[j-1], aList[j]
            else:
                break  # 삽입정렬의 자이
    return aList


li = [23, 78, 45, 8, 32, 56]
print(sort(li))