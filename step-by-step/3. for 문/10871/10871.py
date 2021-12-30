# import sys
# input = sys.stdin.readline

# result = []

# N, X = map(int, input().split())
# A = input().split()
# for i in A:
#     if int(i) < X:
#         result.append(i)

# print(' '.join(result))


##################

a,b = map(int,input().split())
score = [x for x in input().split() if int(x)<b]
print(' '.join(score))