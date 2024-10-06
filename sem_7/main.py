# # Задание 1. Функцию группового переименования файлов.
# import os
# def batch_rename_files(directory, final_name, num_digits, old_extension, new_extension,name_range):
#     if not os.path.isdir(directory):
#         raise FileNotFoundError(f"Каталог '{directory}' не найден.")
#
#     files = [f for f in os.listdir(directory) if f.endswith(old_extension)]
#
#     if not files:
#         print("Файлы с указанным расширение не найдены.")
#
#         return
#
#     format_string = f"{{:0{num_digits}d}}"
#
#     for index, file_name in enumerate(files, start=1):
#         base_name = os.path.splitext(file_name)[0]
#
#         if name_range:
#             start, end = name_range
#             extracted_name = base_name[start-1:end]
#         else:
#             extracted_name = base_name
#
#         new_file_name = f"{extracted_name}{final_name}{format_string.format(index)}{new_extension}"
#
#         old_file_path = os.path.join(directory,file_name)
#         old_file_path = os.path.join(directory, new_file_name)
#         os.rename(old_file_path, old_file_path)
#         print(f"Переименован '{file_name}' в '{new_file_name}'")
#
# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 6:
#         print("Usage: python file_rename.py <directory> <final_name> <num_digits> <old_extension> <new_extension>")
#         sys.exit(1)
#
#     directory = sys.argv[1]
#     final_name = sys.argv[2]
#     num_digits = int(sys.argv[3])
#     old_extension = sys.argv[4]
#     new_extension = sys.argv[5]
#
#     name_range = [3, 6]
#
#     batch_rename_files(directory,final_name, num_digits, old_extension, new_extension,name_range)
#
# # Задача 2. Создание архива каталога
# import os
# import zipfile
#
# def zip_directory(source_dir, output_zip):
#     with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         for root, dirs, files in os.walk(source_dir):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 zipf.write(file_path,os.path.relpath(file_path, source_dir))
#
#
# zip_directory('/path/to/source_dir', '/path/to/output.zip')
#
#
# # Задача 3. Удаление старых файлов
# import  os
# import time
#
# def delete_old_files(directory, days_old):
#     now = time.time()
#     cutoff = now - (days_old * 86400)
#     for root, dirs,files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             file_mod_time = os.path.getmtime(file_path)
#             if file_mod_time < cutoff:
#                 os.remove(file_path)
#                 print(f"Удален файл: {file_path}")
#
#
# delete_old_files('/path/to/directory', 30)
#
#
# # Задача 4. Поиск файлов по расширению
import os

def find_files_by_extension(directory, extension):
    for root, dirs, files, in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))



find_files_by_extension('/path/to/directory', '.txt')





