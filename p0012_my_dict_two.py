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

# Проверка наличия ключа "country" в словаре
if "country" in my_dict:
    print("Ключ 'country' найден в словаре.")
else:
    print("Ключ 'country' не найден в словаре.")

# Вывод всех ключей и значений из словаря
print("\nКлючи и значения из словаря my_dict:")
for key, value in my_dict.items():
    print(f"Ключ: {key}, Значение: {value}")

