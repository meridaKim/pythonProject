if __name__ == "__main__":
    num = int(input())
    dp = [0] * (num +1)
    dp[1] =1
    dp[2] =1

    for i in range(3, num+1):
        dp[i] = dp[i-1]+dp[i-2]

    print(dp[num])