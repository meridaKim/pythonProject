N = int(input())
array = []
for i in range(N) :
    classtime = input().split()
    array.append((int(classtime[0]),int(classtime[1])))

def start(classtime):
    return classtime[0]
def end(classtime):
    return classtime[1]
endresult = sorted(array, key=end)
startresult = sorted(endresult, key=start)



# last = 0
# cnt = 0
# for i, j in endresult:
#     if i >= last:
#         cnt += i
#         last = j
# print(cnt)

print(endresult)
print(startresult)
