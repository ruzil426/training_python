import os
import time

directory = os.getcwd()
for address, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(address, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(file_path)
        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size}, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')