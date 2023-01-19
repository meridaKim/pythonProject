N, L, H = map(int, input().split())
score = sorted(list(map(int, input().split())))
final = sum(score[L:(N - H)]) / (N - L - H)
print(final)