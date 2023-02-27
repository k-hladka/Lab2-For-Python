numbers = []
countPositive = 0
for i in range(3):
    numbers.append(float(input("Введіть число: ")))
    if (numbers[i] > 0):
        countPositive += 1

print(f"Ви ввели {countPositive} позитивних числа")
