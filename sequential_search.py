
def sequential_search(n,target,array):
        for i in range(n):
            if array[i]== target:
                return i + 1
                #인덱스는 0부터 시작하므로!
print("생성 원소 개수 입력 후 스페이스 입력 후 검색할 문자열 입력하세요")

input_data = input().split()
n = int(input_data[0])
target = int(input_data[1])

print("원소 개수만큼 문자열 입력하세요")
array = input().split()

print(sequential_search(n,target,array))