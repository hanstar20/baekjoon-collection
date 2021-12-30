'''
하나씩 소수 판별하는 방법 - 이걸로는 힘들다. 시간 초과가 걸림
'''

# M = int(input())
# N = int(input())

# result = []

# for i in range(M, N+1):
#     price_number = True
#     if i != 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 price_number = False
#         if price_number:
#             result.append(i)

# if len(result) == 0:
#     print(-1)
# else:
#     print(sum(result))
#     print(min(result))

'''
아라토스테네스의 체를 이용해보자
'''

import math

M = int(input())
N = int(input())

def solution(min_num ,max_num):
    numbers = [True] * (max_num + 1)
    answer = []

    for num in range(2,int(math.sqrt(max_num))+1):
        if numbers[num] == False:
            continue;

        for i in range(num+num,max_num+1,num):
            numbers[i] = False

    for i in range(2,max_num+1):
        if numbers[i] == True:
            if i >= min_num:
                answer.append(i)
    
    return answer

result = solution(M,N)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))




