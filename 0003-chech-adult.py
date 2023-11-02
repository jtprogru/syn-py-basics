def check_adult():
    age = int(input("Введите ваш возраст: "))

    if age >= 18:
        print("Вы совершеннолетний(я)")
    else:
        print("Вы несовершеннолетний(я)")

check_adult()  # Вызов функции для запуска программы

