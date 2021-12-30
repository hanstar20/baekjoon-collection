N = int(input())

P = []
for j in range(N):
    P.append([int(i) for i in input().split()])

result = []
for i in range(N):
    k = 0
    for j in range(N):
        if i != j:
            if P[i][0] < P[j][0] and P[i][1] < P[j][1]:
                k += 1
    result.append(k+1)

for res in result:
    print(res)

