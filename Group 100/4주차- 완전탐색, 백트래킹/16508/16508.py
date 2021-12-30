import sys

input = sys.stdin.readline

word = input().strip()
N = int(input())
books = []
for _ in range(N):
    price, book = input().split()
    books.append([int(price), book])

def check_word(word, book_str, price):
    cnt = 0
    for w in word:
        if w in book_str:
            cnt += 1
            book_str = book_str.replace(w, ' ',1)
            if cnt == len(word):
                return price
    return sys.maxsize


result = []

for i in range(1 << N):
    search_str = ""
    sum_price = 0
    for j in range(N):
        if (i & 1 << j) != 0:
            search_str += books[j][1]
            sum_price += books[j][0]

    result.append(check_word(word, search_str, sum_price))

result = min(result)
if result == sys.maxsize:
    result = -1

print(result)
    

# import sys

# input = sys.stdin.readline

# in_str = input()
# bcnt = int(input())
# price = []
# in_major = []
# for i in range(bcnt):
#     p, m = input().split()
#     price.append(int(p))
#     in_major.append(m)

# def wordinbook(word, book, price):
#     cnt = 0
#     for w in word:
#         if w in book:
#             cnt += 1
#             book = book.replace(w, ' ', 1) # 오려낸 글자는 없애준다
#             # print(book, word)
#             if cnt == len(word):
#                 return price
#     return sys.maxsize

# result = []

# for i in range(1 << len(in_major)):
#     search_str = ""
#     sum_price = 0
#     for j in range(len(in_major)):
#         # print(i, j,"/",i&1, i & 1 << j)
#         if (i & 1 << j) != 0: # 
#             # print(in_major[j])
#             search_str += in_major[j]
#             sum_price += price[j]
#     print(search_str)

#     result.append(wordinbook(in_str, search_str, sum_price))

# result = min(result)
# if result == sys.maxsize:
#     result = -1

# print(result)