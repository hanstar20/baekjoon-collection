N = int(input())

for j in range(N):
    digits = [int(i) for i in str(j)]
    if j + sum(digits) == N:
        print(j)
        exit()

print(0)