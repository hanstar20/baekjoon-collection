N, M = map(int, input().split())

result = 0

cards = [int (i) for i in input().split()]

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_cards = cards[i] + cards[j] + cards[k]
            if sum_cards <= M:
                result = max(result, sum_cards)

print(result)