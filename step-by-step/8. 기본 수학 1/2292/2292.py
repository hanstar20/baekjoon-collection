N = int(input())

standard = 1
layer = 1
while True:
    if N == 1:
        print(1)
        break

    standard = standard + 6*layer
    if standard >= N:
        print(layer + 1)
        break
    layer += 1


# ===============================

a=int(input())
i=s=1
while s<a:
	s+=6*i
	i+=1
print(i)