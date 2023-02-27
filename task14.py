from math import pow

N = int(input("Введіть число N>1: "))

i = 1
while i:
    if (pow(5, i) > N):
        K = i
        break
    i += 1

print(f"Ви ввели невірне число! ") if N<=1 else print(f"Найменше K, що задовільняє умову 5^K>N = {K}")
