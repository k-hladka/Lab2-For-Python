a = int(input("Введіть число a: "))

sum = 0
for i in range(a, 51):
    sum += i**2

print(f"Сума квадратів від {a} до 50 = {sum}")