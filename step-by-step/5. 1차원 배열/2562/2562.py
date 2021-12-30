Num = []
for i in range(9):
    Num.append(int(input()))

print(max(Num))
print(Num.index(max(Num)) + 1)


###########################

Num = [int(input()) for i in range(9)]
print(max(Num), Num.index(max(Num)) + 1)
