class Product:
            def __init__(self, title, price, quantity):
                self.title = title
                self.price = price
                self.quantity = quantity

            def __str__(self):
                return f"Описание продукта: \n Название: {self.title}, \n Цена: {self.price}, \n Количество: {self.quantity}"

            def __repr__(self):
                return f"Product(title='{self.title}', price='{self.price}', quantity='{self.quantity}'"

            def __eq__(self, other):
                return self.title == other.title

            def __lt__(self, other):
                return self.price < other.price

            def __add__(self, other):
                return Product(
                        title="Combo",
                        price=self.price + other.price,
                        quantity=1
                        )

p1 = Product("Блеск для губ Dior", 4000, 20)
p2 = Product("Палетка теней Hourglass", 10500, 15)
p3 = Product("Скраб для тела ACT", 900, 5)

print(p1 == p2)
print(p3 < p2)
combo = p2 + p3
print (combo)