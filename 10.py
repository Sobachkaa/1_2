# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
def min_flips(coins):
    heads = coins.count('H')
    tails = coins.count('T')
    if heads == 0 or tails == 0:
        return 0
    elif heads == tails:
        return heads
    else:
        return abs(heads - tails)

n = int(input())
coins = input().split()
print(min_flips(coins))