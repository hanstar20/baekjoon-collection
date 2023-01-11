A, B = map(int, input().split())
C = int(input())

plus_hour = C//60
plus_min = C % 60


min = B + plus_min

hour = (A + plus_hour + min//60) % 24
min = min % 60

print(f'{hour} {min}')
