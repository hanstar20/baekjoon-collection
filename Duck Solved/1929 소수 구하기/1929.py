M, N = map(int, input().split())


def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1

    return arr


arr = is_prime_num(N)

for i in range(len(arr)):
    if arr[i] == True:
        if i >= M:
            print(i)
