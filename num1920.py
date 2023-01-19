N = int(input())
target_list = sorted(list(map(int, input().split())))
M = int(input())
search_list = sorted(list(map(int, input().split())))
def searching_z(target):
      target = target_list[i]
      left, right = 0, N - 1
      while left <= right:
            mid = (left + right) // 2
            if mid == target:
                return 1

            elif target <= mid:
                right = mid -1
            else:
               left = mid +1

for i in range(M):
    if searching_z(search_list[i]):
        print(1)
    else:
        print(0)