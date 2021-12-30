self_num = list(range(1,10001))
for i in range(1,10001):
    sum_num = 0
    for a in str(i):
        sum_num += int(a)
    result = i + sum_num
    if self_num.count(result) != 0:
        self_num.remove(result)

for i in self_num:
    print(i)