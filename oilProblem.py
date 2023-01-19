N = int(input())
roads = list(map(int,input().split()))
price= list(map(int,input().split()))

minVal = price[0]
#가장 작은 주유비를 가진 도시를 첫번째로
sum = 0

for i in range(N-1):
    #마지막 도시 제외한 n-1 도시의 수만큼 반복
    if minVal > price[i]:
        #최소금액이 현 도시의 금액보다 크면
        minVal = price[i]
        #최소금액을 현 도시의 금액으로 바꾼다(최소라는 조건을 유지하기 위해)
    sum +=(minVal * roads[i])

print(sum)

