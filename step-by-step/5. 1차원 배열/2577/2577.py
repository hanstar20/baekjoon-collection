A = int(input())
B = int(input())
C = int(input())

mul_str = str(A * B * C )

result = [mul_str.count(str(i)) for i in range(10)]

for i in range(10):
    print(result[i])