import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    print(sum(map(int, input().split())))