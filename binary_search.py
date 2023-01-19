def binary_search(array, target, start,end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)
        ##중간값이 타겟보다 크면 중간값 기준 오른쪽은 모두 타켓보다 크므로 왼쪽 탐색(end를 mid-1로 대체)
    else :
        return binary_search(array,target,mid+1, end)
        ##중간값이 타겟보다 작으면 중간값 기준 왼쪽은 모두 타켓보다 작으므로 오른쪽 탐색(start를 mid+1로 대체)

    n, target = list(map(input().split()))

    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("원소 존재하지 않음")
    else:
        print(result + 1)