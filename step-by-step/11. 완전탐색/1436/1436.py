N = int(input())

result = 0

for i in range(666, 10000000):
    if '666' in str(i):
        result += 1
    
    if result == N:
        print(i)
        break