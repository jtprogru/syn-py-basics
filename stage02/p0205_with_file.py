def main():
    # Создаем текстовый файл и записываем в него данные
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write("Пример текстового файла\n")
        file.write("Вторая строка файла\n")
        file.write("Третья строка файла\n")

    # Читаем содержимое файла и выводим его на экран
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Содержимое файла:\n", content)


if __name__ == "__main__":
    main()
