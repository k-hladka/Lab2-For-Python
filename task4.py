from math import cos

arr = []
for i in range(4):
    arr.append(float(input(f"Введіть {i + 1} із 4-х чисел: ")))
    if (i == 0 or min > arr[i]):
        min = arr[i]

print(f"Косинус мінімального з чисел ({min}) = {cos(min * 3.14 / 180)}")