print("Введіть сторони рівнобедренного трикутника: ")
triangle = []
perimetr = 0
for i in range(3):
    triangle.append(int(input()))
    perimetr += triangle[i]

perimetr /= 2
area = (perimetr * (perimetr - triangle[0]) * (perimetr - triangle[1]) * (perimetr - triangle[2])) ** 0.5
if (area % 2 == 0):
    area /= 2
    print(f"Площа трикутника = {area}")
else:
    print(f"Не можу ділити на 2! Площа трикутника = {area}")