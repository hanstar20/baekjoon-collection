N = int(input())

def factorial(Number):
    if Number == 0:
        return 1
    return Number * factorial(Number-1)

print(factorial(N))