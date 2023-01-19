M = int(input())
def my_factorial(n):
    for i in range(11):
        if(n > 1):
            return n * my_factorial(n - 1)
        else:
            return 1
print(my_factorial())