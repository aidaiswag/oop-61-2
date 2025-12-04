class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health
    def info(self) -> str:
        return f"{self.name}, {self.age} лет, здоровье {self.health}"
    def use_ability(self):
        return f"{self.name} использует базовую способность."


class Flyable:
    def use_ability(self):
        return super().use_ability() + " летает."


class Swimmable:
    def use_ability(self):
        return super().use_ability() + " плавает."


class Invisible:
    def use_ability(self):
        return super().use_ability() + " становится невидимым."

class Duck(Flyable, Swimmable, Animal):
    pass

class Bat( Invisible,Flyable, Animal):
    pass

class Frog( Swimmable, Animal):
    pass

class Phoenix(Invisible, Flyable, Animal):
    def reborn(self):
        return f"{self.name} перерождается."

class Zoo:
    def __init__(self):
        self.animals = []
    def add_animal(self, animal: Animal):
        self.animals.append(animal)
    def show_all(self):
        for animal in self.animals:
            print(animal.info())
    def perform_show(self):
        for animal in self.animals:
            print(animal.use_ability())


if __name__ == "__main__":
    zoo = Zoo()

    duck = Duck("Дональд", 3, 80)
    bat = Bat("Бэтти", 5, 60)
    frog = Frog("Кермит", 2, 50)
    phoenix = Phoenix("Феникс", 100, 200)

    for animal in (duck, bat, frog, phoenix):
        zoo.add_animal(animal)

    print("=== Информация о животных ===")
    zoo.show_all()

    print("\n=== Шоу суперспособностей ===")
    zoo.perform_show()

    print("\nMRO для Duck:", Duck.mro())
    print("MRO для Phoenix:", Phoenix.mro())