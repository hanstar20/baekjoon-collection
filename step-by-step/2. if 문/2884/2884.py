# 첫 번째 방법
# H, M = map(int, input().split())

# if M < 45:
#     if H == 0:
#         H = 23
#     else :
#         H -= 1
#     M += 15
# else:
#     M = M - 45

# print(H, M)

# 두 번쟤 방법
H,M=map(int,input().split())
M=H*60+M-45
print(M//60%24, M%60)
