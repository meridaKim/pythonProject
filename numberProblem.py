N = int(input())
a=[]
a = [0 for i in range(N)]
for i in range(len(a)):
    if(N%10==0):
        print(N)
    else:
        for j in range(len(a)):
            a.append(N%10)
    result = sum(a)

n = N-result

print(n)