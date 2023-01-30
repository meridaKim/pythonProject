def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        if memorization[n] != 0:
            return memorization[n]
        else:
            memorization[n] = fibo(n-1)+ fibo(n-2)
            return memorization[n]

if __name__ == "__main__":
    num = 5
    memorization = [0] * (num+1)
    print(fibo(num))