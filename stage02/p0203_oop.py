class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(self.__str__())

    def __str__(self):
        return f"Car Info: {self.year} {self.make} {self.model}"


def main():
    # Пример использования класса
    car1 = Car("Toyota", "Camry", 2020)
    car1.display_info()

    car2 = Car("Honda", "Civic", 2019)
    car2.display_info()


if __name__ == "__main__":
    main()