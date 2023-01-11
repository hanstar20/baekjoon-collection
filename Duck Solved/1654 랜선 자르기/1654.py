K, N = map(int, input().split())
arr = []
for i in range(K):
    arr.append(int(input()))


for i in range(max(arr)+1, 1, -1):
    result = 0
    for num in arr:
        result += num//i

    if result >= N:
        print(i)
        break
