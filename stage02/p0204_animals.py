class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Гав")


class Cat(Animal):
    def make_sound(self):
        print("Мяу")


def main():
    # Пример использования классов
    dog1 = Dog("Buddy", "Dog")
    dog1.make_sound()

    cat1 = Cat("Whiskers", "Cat")
    cat1.make_sound()


if __name__ == "__main__":
    main()