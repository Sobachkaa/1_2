def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b//2) * power(a, b//2)
    else:
        return a * power(a, b//2) * power(a, b//2)

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(power(a, b))