from itertools import combinations

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append([int(x) for x in input().split()])


# 치킨이 1개일 때
result = 0
for i in range(M):
    sum_a = 0
    for people in A:
        sum_a += people[i]
    result = max(result, sum_a)

# 치킨이 2개일 때
coms = combinations(list(range(M)), 2)
for com in coms:
    sum_a = 0
    for people in A:
        sum_a += max(people[com[0]], people[com[1]])
    result = max(result, sum_a)

# 치킨이 2개일 때
coms = combinations(list(range(M)), 3)
for com in coms:
    sum_a = 0
    for people in A:
        sum_a += max(people[com[0]], people[com[1]], people[com[2]])
    result = max(result, sum_a)

print(result)