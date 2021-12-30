import sys
input = sys.stdin.readline

T = int(input())
A = list(map(int, input().split()))
Max_A = max(A)
Min_A = min(A)
print(Min_A, Max_A)
    