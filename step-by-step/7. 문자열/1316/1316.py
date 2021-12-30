words = []
group_word = 0

N = int(input())

for i in range(N):
    words.append(input())


for word in words:
    _list_word = list(word)

    while True :
        check_alp = _list_word.pop(0)
        if len(_list_word) == 0:
            group_word += 1
            break
        if check_alp != _list_word[0]:
            if check_alp in _list_word:
                break

print(group_word)

