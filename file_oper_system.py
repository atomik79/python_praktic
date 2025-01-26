import os
import time


def module_os(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_time = os.path.getmtime(file_path)
            file_time_formatted = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
            file_size = os.path.getsize(file_path)
            parent_dir = os.path.dirname(file_path)
    #print(f"есть файл: {file}")
    #print(f"путь к файлу:{file_path}")
    #print(f"размер: {file_size}")
    #print(f"modified time: {file_time_formatted}")
    #print(f"родительская directory: {parent_dir}")
    #print("-" * 20)
    '''print(f"есть файл: {file} путь к файлу:{file_path} размер: {file_size} "
          f"modified time: {file_time_formatted} родительская directory: {parent_dir}")'''
    print(f"есть файл: {file}", f" путь к файлу:{file_path}", f"размер: {file_size}",
          f"modified time: {file_time_formatted}", f" родительская directory: {parent_dir}", sep="\n")


'''if __name__ == '__main__':
    module_os(".")'''
module_os(".")