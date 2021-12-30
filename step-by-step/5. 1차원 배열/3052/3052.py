A = []
result = 0
for i in range(10):
    A.append(int(input())%42)

for i in range(42):
    if A.count(i) != 0:
        result += 1

print(result)


############################

b = [int(input())%42 for i in range(10)]
print(len(set(b)))