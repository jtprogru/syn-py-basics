"""
Домашнее задание
"""


# Создание пустого словаря
my_dict = {}

# Добавление элементов в словарь
my_dict["name"] = "John"
my_dict["age"] = 25
my_dict["city"] = "New York"

# Вывод содержимого словаря
print("Содержимое словаря my_dict:")
print(my_dict)

# Изменение возраста в словаре
my_dict["age"] = 26

# Добавление ключа "email" в словарь
my_dict["email"] = "john@example.com"

# Удаление ключа "city" из словаря
my_dict.pop("city", None)

# Вывод всех ключей и значений из словаря
print("\nКлючи и значения из словаря my_dict:")
for key, value in my_dict.items():
    print(f"Ключ: {key}, Значение: {value}")
