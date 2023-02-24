price = float(input("Введіть ціну товару: "))
if (price >= 500 and price < 1000):
    price -= price * 0.03
elif (price >= 1000):
    price -= price * 0.05
print(f"Ціна товару зі знижкою = {price}")