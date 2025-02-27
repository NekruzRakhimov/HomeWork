import os

# 1. Работа с модулем os
# Есть папка, в которой лежат файлы с разными расширениями.
# Программа должна:
# ● Вывести имя вашей ОС
print("Имя операционной системы:", os.name)

# ● Вывести путь до папки, в которой вы находитесь
current_directory = os.getcwd()
print("Путь до папки:", current_directory)

# ● Рассортировать файлы по расширениям, например, для
# текстовых файлов создается папка, в неё перемещаются
# все файлы с расширением .txt, то же самое для остальных
# расширений
files_by_extension = {}
for filename in os.listdir(current_directory):
    if os.path.isfile(filename):  # Проверяем, что это файл
        extension = os.path.splitext(filename)[1]  # Получаем расширение
        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(filename)

# ● После рассортировки выводится сообщение типа «в папке
# с текстовыми файлами перемещено 5 файлов, их
# суммарный размер - 50 гигабайт»
for extension, files in files_by_extension.items():
    folder_name = extension.lstrip('.') + '_files'  # Имя папки
    os.makedirs(folder_name, exist_ok=True)  # Создание папки, если не существует

    total_size = 0
    for file in files:
        file_path = os.path.join(current_directory, file)
        total_size += os.path.getsize(file_path)  # Суммируем размер файлов

        # Перемещение файла с использованием os.rename
        new_file_path = os.path.join(folder_name, file)
        os.rename(file_path, new_file_path)

    print(
        f"В папке с файлами {folder_name} перемещено {len(files)} файлов, их суммарный размер - {total_size / (1024 ** 3):.2f} гигабайт"
        # f"В папке с файлами {folder_name} перемещено {len(files)} файлов, их суммарный размер - {total_size / 1024:.2f} килобайт"
        # f"В папке с файлами {folder_name} перемещено {len(files)} файлов, их суммарный размер - {total_size:.2f} байт"
    )

    # ● Как минимум один файл в любой из получившихся
    # поддиректорий переименовать. Сделать вывод
    # сообщения типа «Файл data.txt был переименован в
    # some_data.txt»

    if files:
        old_file_path = os.path.join(folder_name, files[0])
        new_file_name = f"renamed_{files[0]}"
        new_file_path = os.path.join(folder_name, new_file_name)
        os.rename(old_file_path, new_file_path)
        print(f"Файл {files[0]} был переименован в {new_file_name}")

# ● Программа должна быть кроссплатформенной – никаких
# хардкодов с именем диска и слэшами.
