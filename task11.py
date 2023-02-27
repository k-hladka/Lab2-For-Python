a = int(input("Введіть число А: "))
b = int(input("Введіть число B: "))

sum = 0
countNumber = 0
for i in range(a, b + 1):
    countNumber+=1
    sum += i

avg = sum/countNumber
print(f"Середнє арифметичне чисел = {avg}")