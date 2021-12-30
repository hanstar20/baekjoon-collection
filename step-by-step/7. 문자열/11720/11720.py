N = input()
num = input().strip()
result = 0
for i in num:
    result += int(i)
print(result)

#######################################

input()
print(sum(map(int, input())))