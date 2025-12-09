class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! Mp: {self.mp}"


class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    def __init__(self, bank_name, balance, password):
        self.bank_name = bank_name
        self._balance = balance
        self.__password = password

    def login(self, password):
        if password == self.__password:
            return "Проверка прошла успешно!"
        return "Неверный пароль"

    def full_info(self):
        return f"Имя: {self.name}, уровень: {self.lvl}, здоровье: {self.hp}, баланс: {self._balance}"

    def get_bank_name(self):
        return self.bank_name

