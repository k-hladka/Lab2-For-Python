year = int(input("Введіть номер року: "))
if (year % 400 == 0 and year % 100 == 0):
    print("Цей рік є високосним")
else:
    print("Цей рік не є високосним")