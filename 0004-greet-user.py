def greet_user():
    name = input("Введите ваше имя: ")

    if name:
        print(f"Привет, {name}!")
    else:
        print("Вы не ввели имя.")

greet_user()  # Вызов функции для запуска программы

