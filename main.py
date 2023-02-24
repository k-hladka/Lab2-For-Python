# ***************      Task1       ****************
number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
number3 = int(input("Введіть третє число: "))

arr = [number1, number2, number3]

for i in arr:
    if(i>=1 and i<=3):
        print(i)

# ***************      Task2       ****************
year = int(input("Введіть номер року: "))
if(year%400 == 0 and year%100==0):
    print("Цей рік є високосним")
else:
    print("Цей рік не є високосним")

# ***************      Task3       ****************
price = float(input("Введіть ціну товару: "))
if(price>=500 and price<1000):
    price-=price *0.03
elif (price>=1000):
    price-= price* 0.05
print(f"Ціна товару зі знижкою = {price}")