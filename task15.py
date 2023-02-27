n = int(input("Введіть число n: "))

for i in range(n + 1):
    if (i ** 2 > n):
        print(f"Перше з чисел, яке більше {n} = {i ** 2}")
        break
