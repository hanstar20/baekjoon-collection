import math
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    x = math.ceil(N / H)
    y = H if N % H == 0 else (N % H)
    print(y, end='')
    if x < 10:
        print(f'0{x}')
    else :
        print(x)