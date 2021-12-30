N = int(input())

Num = map(int, input().split())
result = 0
for i in Num:
    price_number = True
    if i != 1:
        for j in range(2,i):
            if i % j == 0:
                price_number = False
        if price_number:
            result += 1

print(result)
        