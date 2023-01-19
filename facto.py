def facto(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros


m = int(input())
left, right, result = 1, m * 5, 0

while left <= right:
    mid = (left + right) // 2

    zero_count = facto(mid)


    if zero_count < m:
        left = mid + 1
        #m=3일때, zero_count = 2, left = 9
    else:
        right = mid - 1
       #m=3일때, zero_count = 3, right = 11
        result = mid
        #mid = 10

print(result if facto(result) == m else -1)