A = int(input("Введіть число А: "))
B = int(input("Введіть число B: "))

sum = 0
for i in range(A, B + 1):
    sum += i**2
    print(i**2)

print(sum)