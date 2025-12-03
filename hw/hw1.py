class Pizza:
    def __init__(self, name, size, sauce):
        self.name = name
        self.size = size
        self.sauce = sauce
    def cheese(self):
        return f"В пиццу {self.name} добавлен сыр."
    def info(self):
        return f"Название-{self.name}, размер-{self.size}, соус-{self.sauce}"

pizza1 = Pizza("Маргарита", 40, "Томатный")
pizza2 = Pizza("Пепперони", 60, "Песто")
print(pizza1.cheese())
print(pizza2.cheese())
print(pizza1.info())