calphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in calphabet:
    word = word.replace(i, "_")

print(len(word))

