def check_ticket():
    age = int(input("Введите ваш возраст: "))
    accompanied = input("Есть ли у вас сопровождающий? (да/нет): ").lower()

    if age < 12:
        print("Билет бесплатный")
    elif 12 <= age <= 18 and accompanied == 'да':
        print("Билет со скидкой")
    else:
        print("Полная стоимость билета")

check_ticket()  # Вызов функции для запуска программы

