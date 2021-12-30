N = int(input().strip())
result = 0
for i in range(1, N+1):
    if i < 100:
        result += 1
    else :
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2])    :
            result += 1

print(result)
