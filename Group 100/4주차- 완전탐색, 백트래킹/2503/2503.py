import itertools


N = int(input())

data = []
for j in range(N):
    data.append([int(i) for i in input().split()])

def check(case, numbers):
    strike = 0
    ball = 0
    for idx_num, number in enumerate("{}".format(numbers)):
        for idx_case, case_num in enumerate("{}".format(case[0])):
            if number == case_num:
                if idx_case == idx_num:
                    strike += 1
                else:
                    ball += 1
    if case[1] == strike and case[2] == ball: return True
    else: return False

result = []
samples = itertools.permutations(['1','2','3','4','5','6','7','8','9'], 3)
num = []
for sample in samples:
    str = ''.join(sample)
    num.append(int(str))

for i in num:
    possible = True
    for case in data:
        possible = check(case, i)
        if possible == False:
            break
    if possible == True:
        result.append(i)

print(len(result))
