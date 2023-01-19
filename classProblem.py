import heapq
N = int(input())
q =[]
for i in range(N):
    S,T= list(map(int, input().split()))
    q.append([S,T])

q.sort()
#시작시간과 종료시간을 q에 입력 후 리스트 q 오름차순 정렬
room = []
heapq.heappush(room,q[0][1])

for i in range(1,N):
    if q[i][0]<room[0]:
        #다음 시작 시간보다 끝나는 시간이 더 늦으면 heappush로 추가
        heapq.heappush(room,q[i][1])
    else:
        #다음 시작 시간보다 끝나는 시간이 더 빠르면 heappop으로 제거 후 기존 강의실 사용하기 위해 heappush로 추가
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])

print(len(room))
