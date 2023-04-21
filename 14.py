# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input())
for k in range(0, n+1):
    power = 2**k
    if power <= n:
        print(power)
    else:
        break