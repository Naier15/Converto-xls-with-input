import os

# Запрашиваем путь к файлу
path = input('Введите абсолютный путь к файлу: ')

# Берем название файла и поучаем его расширение
path2 = path.rsplit('\\', maxsplit=1)
extension = path2[-1].split('.')

# Меняем расширение
extension[1] = '.xls'
new_filename = extension[0] + extension[1]

# Пересохраняем
old_track = path2[0] + '\\' + path2[1]
new_file = path2[0] + '\\' + new_filename
os.rename(old_track, new_file)
