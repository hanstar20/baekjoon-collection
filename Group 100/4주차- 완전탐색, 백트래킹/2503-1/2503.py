import sys
import itertools

input = sys.stdin.readline

N = int(input())

data = []
for _ in range(N):
    num, s, b = map(int, input().split())
    data.append([num, s, b])

def check(case, number):
    strike = 0
    ball = 0
    num, s, b = case
    for idx, digit in enumerate(number):
        for idx_case, digit_case in enumerate(str(num)):
            if digit == digit_case:
                if idx == idx_case:
                    strike += 1
                else:
                    ball += 1
    if s == strike and b == ball:
        return True
    else:
        return False

result = []

nPr = list(itertools.permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

for number in nPr:
    possible = True
    for case in data:
        possible = check(case, number)
        if possible == False:
            break
    if possible == True:
        result.append(number)

print(len(result))
