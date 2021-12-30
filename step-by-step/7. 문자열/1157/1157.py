import string
upper = string.ascii_uppercase
count = []

String = input().upper()
for al in upper:
    if al in String:
        count.append(String.count(al))
    else :
        count.append(0)
if count.count(max(count)) > 1:
    print('?')
else :
    print(upper[count.index(max(count))])
