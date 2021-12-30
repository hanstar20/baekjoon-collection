# 첫 번째 방법
# num1 = int(input())
# num2 = input()

# num3 = num1 * int(num2[2])
# num4 = num1 * int(num2[1])
# num5 = num1 * int(num2[0])

# num6 = num3 + (num4 * 10) + (num5 * 100)

# print(num3)
# print(num4)
# print(num5)
# print(num6)


# 두 번째 방법
num1 = int(input())
num2 = input()

for i in reversed(num2):
    print(num1 * int(i))

print(num1 * int(num2))



