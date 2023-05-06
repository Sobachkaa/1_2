def RLE(s):
    if not s.isalpha():
        raise ValueError("Строка должна состоять только из букв A-Z")
    if not s:
        return ""
    result = ""
    count = 1
    for i in range(len(s)):
        if i == len(s) - 1:
            result += s[i] + str(count)
        elif s[i] == s[i+1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1
    return result

s = input("Введите строку: ")
print(RLE(s))