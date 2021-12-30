N = int(input())

Next_N = None
D = 0

while True:
    if N == Next_N:
        print(D)
        break
    
    if D == 0:
        Next_N = N
    
    Next_N = ((Next_N % 10) * 10) + (((Next_N // 10) + (Next_N % 10))%10 )
    D += 1