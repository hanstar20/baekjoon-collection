x, y, w, h = map(int, input().split())

minX = min(x, w-x)

minY = min(y, h-y)

dis = min(minX, minY)

print(dis)