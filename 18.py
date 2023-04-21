# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input())
a = list(map(int, input().split()))
x = int(input())

closest = a[0]
diff = abs(x - a[0])

for i in range(1, n):
    if abs(x - a[i]) < diff:
        closest = a[i]
        diff = abs(x - a[i])

print(closest)