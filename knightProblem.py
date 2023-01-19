n=input()

x = int(n[1])
y = int(ord(n[0]))-int(ord('a'))+1
r = input().split()

dx=[1,2,3,4,5,6,7,8]
dy=["a","b","c","d","e","f","g","h"]
move_types=[(-2,1),(-1,2),(2,1),(1,2),(-2,-1),(-1,-2),(2,-1),(1,-2)]

for i in range(len(move_types)):
    nx = x+dx[i]