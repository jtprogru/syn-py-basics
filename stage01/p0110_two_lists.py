"""
Домашнее задание
"""


# Ввод чисел для первого и второго списка
first_list = input("Введите числа для первого списка через пробел: ").split()
second_list = input("Введите числа для второго списка через пробел: ").split()

# Преобразование ввода в списки чисел
first_list = [int(num) for num in first_list]
second_list = [int(num) for num in second_list]

# Подсчет количества пересекающихся чисел
intersection_count = len(set(first_list).intersection(second_list))

# Вывод результата
print(f"Количество пересечений: {intersection_count}")
