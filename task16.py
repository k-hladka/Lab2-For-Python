n = int(input("Введіть число n: "))

increment = 1
resultNumber = 1
while resultNumber<=n:
    resultNumber+=increment
    increment+=2

print(f"Перше число, яке більше n = {resultNumber}")