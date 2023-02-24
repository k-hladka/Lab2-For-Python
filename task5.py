from math import sin

arr2 = []
for i in range(3):
    arr2.append(float(input(f"Введіть {i + 1} із 3-х чисел: ")))
    if (i == 0 or max < arr2[i]):
        max = arr2[i]
print(f"Cинус максимального з чисел ({max}) = {sin(max * 3.14 / 180)}")