N = int(input())
for i in range(N):
    score = sorted(list(map(int, input().split())))
    score.remove(max(score))
    score.remove(min(score))
    if max(score) - min(score) >= 4:
        print('KIN')
    else :
        # print(max(score))
        # print(min(score))
        final = sum(score[0:])
        print(final)
