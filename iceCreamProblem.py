def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False
#n(행),m(열)값 입력받기
n, m =map(int, input().split())

graph =[]
#빈 그래프 생성 후 n(행)크기의 리스트 만들어 2차원 리스트
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) ==True:
            result +=1
print(result)