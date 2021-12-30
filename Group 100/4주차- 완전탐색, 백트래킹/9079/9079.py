T = int(input())

data = []

for T_idx in range(T):
    for idx in range(3):
        if idx == 0:
            data.append([input().split()])
        else:
            data[T_idx].append(input().split())

def reversal(str):
    if str == 'H':
        return 'T'
    if str == 'T':
        return 'H'

def check(matrix):
    check = matrix[0][0]
    for elements in matrix:
        for element in elements:
            if element != check:
                return False
    return True
                

def change(matrix, case):
    sample = [0, 1, 2, 0 ,1 ,2, 0, 1]
    
    # 열을 변환하는 케이스
    if case >= 0 and case <= 2:
        for i in range(3):
            matrix[sample[case]][i] = reversal(matrix[sample[case]][i])

    # 행을 변환하는 케이스
    if case >= 3 and case <= 5:
        for i in range(3):
            matrix[i][sample[case]] = reversal(matrix[i][sample[case]])

    # 행을 변환하는 케이스
    if case == 6:
        for i in range(3):
            matrix[i][i] = reversal(matrix[i][i])

    if case == 7:
        for i in range(3):
            matrix[i][2 - i] = reversal(matrix[i][2 - i])
    return matrix
        

data[0] = change(data[0], 7)



print(data)
