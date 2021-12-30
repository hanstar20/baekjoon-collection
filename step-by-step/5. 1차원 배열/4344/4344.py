C = int(input())
for i in range(C):
    case = list(map(int, input().split()))
    mean = sum(case[1:])/case[0]
    result = len(list(filter(lambda x:x>mean, case[1:])))/case[0]*100
    print('%.3f' % result + '%')