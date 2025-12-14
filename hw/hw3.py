#Инкапсуляция
class Product:
        def __init__(self, name, price, discount):
            self.name = name
            self._price = price
            self.__discount = discount

        def get_price(self):
            return self._price * (1-self.__discount/100)

        def set_discount(self, percent):
            if percent <= 50:
                self.__discount = percent
            return "Скидка больше 50%!"

        def apply_extra_discount(self, secret_code):
            if secret_code == "VIP123":
                self.__discount += 5
            return "Неверный код!"

a = Product("DiStore Advent Calendar", 35000, 15)

print("Цена со скидкой:", a.get_price())

a.apply_extra_discount("VIP123")
print("Цена после VIP:", a.get_price())

print(a.apply_extra_discount("HAPPY NEW YEAR"))
print("Цена итоговая:", a.get_price())


 #Абстракция
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass

class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата картой: {amount}"
    def refund(self,amount):
        return f"Возврат на карту: {amount}"

class CashPayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата наличными: {amount}"
    def refund(self,amount):
        return f"Возврат наличными: {amount}"

class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        return {"type": "crypto",
                "amount": amount,
                "currency": "USDT"
                }
    def refund(self, amount):
        return {"type": "crypto",
                "amount": amount,
                "currency": "USDT"
                }


class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):
        result = self.payment_method.pay(amount)
        print(result)

processor = PaymentProcessor(CardPayment())
processor.process(1000)
processor = PaymentProcessor(CashPayment())
processor.process(889)
processor = PaymentProcessor(CryptoPayment())
processor.process(6777)