a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

sum = 0

while a:
    sum += a
    if (a == b):
        break
    a += 1

print(sum)
