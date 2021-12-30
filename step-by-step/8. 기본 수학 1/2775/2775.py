result = []
for i in range(15):
    if i == 0:
        result.append(list(range(1,15)))
    else :
        result2 = []
        for j in range(14):
            result2.append(sum(result[i-1][:j+1]))
        result.append(result2)

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(result[k][n-1])