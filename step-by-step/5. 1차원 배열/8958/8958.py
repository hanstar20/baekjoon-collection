N = int(input())
case = []
for i in range(N):
    result = 0
    A = input().split('X')
    for x in A:
        result += sum(range(1,(x.count('O')+1)))
    print(result)

