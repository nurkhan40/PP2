class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        """Метод, который должен быть переопределен в подклассах"""
        pass

    def info(self):
        """Вывод информации о животном"""
        print(f"Это {self.__class__.__name__}, его зовут {self.name}")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав! 🐶")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Мяу-мяу! 🐱")

class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Муууу! 🐮")

dog = Dog("Рекс")
cat = Cat("Мурзик")
cow = Cow("Бурёнка")

dog.info()
dog.make_sound()

cat.info()
cat.make_sound()

cow.info()
cow.make_sound()
