N = int(input())

def Fibonacci(Number):
    if Number == 0:
        return 0
    if Number == 1:
        return 1
    return Fibonacci(Number - 1) + Fibonacci(Number - 2)

print(Fibonacci(N))