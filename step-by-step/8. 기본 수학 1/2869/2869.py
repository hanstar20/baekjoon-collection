import math

A, B, V = map(int, input().split())

gap = A - B
result = math.ceil((V-A) / gap) + 1
print(result)
