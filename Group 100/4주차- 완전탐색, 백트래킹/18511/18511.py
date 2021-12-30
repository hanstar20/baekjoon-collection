from itertools import product

N, M = map(int, input().split())
K_str = input().split()
K = [int(x) for x in K_str]

_list_N = [int(x) for x in str(N)]


# 첫 자리를 통해 자릿수 설정
if len(_list_N) == 2:
    result = 0
    cases = list(product(K_str,repeat = 2))
    for case in cases:
        num = int(''.join(case))
        if num <= N:
            result = max(result, num)
    if result != 0:
        print(result)
        exit()
    else:
        result = max(K)
        print(result)
        exit()

    

if _list_N[0] < min(K):
    length = len(_list_N) - 1
    result = int(str(max(K)) * length)
    
else :
    result = 0
    length = len(_list_N)
    cases = list(product(K_str,repeat = length))
    for case in cases:
        num = int(''.join(case))
        if num <= N:
            result = max(result, num)

print(result)
