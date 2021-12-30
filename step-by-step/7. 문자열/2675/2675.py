T = int(input())
for i in range(T):
    R, S = input().split()
    result = ''
    for al in S:
        result += al * int(R)
    print(result)

