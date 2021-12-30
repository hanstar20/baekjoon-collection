N=int(input())
i=s=1
while s<N:
    i+=1
    s+=i

p = (N - sum(range(1, i))) # 레이어 구하고 몇번쨰임!!
if i % 2 == 0:
    print(f'{p}/{i+1-p}')
else:
    print(f'{i+1-p}/{p}')


