class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
        def __init__(self, name, lvl, hp, mp):
             super().__init__(name, lvl, hp)
             self.mp = mp

        def action(self):
             return f"Маг {self.name} кастует заклинание! Mp: {self.mp}"


class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password):
        if password == self.__password:
            return "Проверка прошла успешно!"
        return "Неверный пароль"

    def full_info(self):
        return f"Имя: {self.hero.name}, уровень: {self.hero.lvl}, здоровье: {self.hero.hp}, баланс: {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        return "Ошибка! Нельзя сложить счета героев разных классов"


mage = MageHero("Merlin", 80, 500, 150)
warrior = WarriorHero("Conan", 50, 900, 0)

acc1 = BankAccount(mage, 5000, "1234", "Simba")
acc2 = BankAccount(warrior, 3000, "1111", "Simba")

print(mage.action())
print(warrior.action())
print(acc1)
print(acc1.full_info())
print(acc1 + acc1)     # работает
print(acc1 + acc2)