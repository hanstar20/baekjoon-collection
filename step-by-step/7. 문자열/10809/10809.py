# import string
# lower = [i for i in string.ascii_lowercase]
# result = []

# word = input()

# for alphabet in lower:
#     if alphabet in word:
#         result.append(str(word.index(alphabet)))
#     else :
#         result.append('-1')

# print(' '.join(result))


#################################
import string
lower = string.ascii_lowercase

word = input()
for i in lower:
    print(word.find(i), end = ' ')
