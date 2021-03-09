import os
import time
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
os_name = input('select your OS: win if windows, lin if linux')
if os_name=='win':
	source = ['"C:\\My Documents"', 'C:\\Code']
	# Заметьте, что для имён, содержащих пробелы, необходимо использовать
	# двойные кавычки внутри строки.
	# 2. Резервные копии должны храниться в основном каталоге резерва.
	target_dir = 'E:\\Backup' # Подставьте ваш путь.
	# 3. Файлы помещаются в zip-архив.
	# 4. Именем для zip-архива служит текущая дата и время.
	target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
	# 5. Используем команду "zip" для помещения файлов в zip-архив
	zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
	# Запускаем создание резервной копии
	if os.system(zip_command) == 0:
		print('Резервная копия успешно создана в', target)
	else:
		print('Создание резервной копии НЕ УДАЛОСЬ')
elif os_name=='lin':
	source = ['"/home/shaggy_axel/PycharmProjects/"', '/home/shaggy_axel/Документы/']
	# Заметьте, что для имён, содержащих пробелы, необходимо использовать
	# двойные кавычки внутри строки.
	# 2. Резервные копии должны храниться в основном каталоге резерва.
	target_dir = '/home/shaggy_axel/my_backups_app/' # Подставьте ваш путь.
	# 3. Файлы помещаются в zip-архив.
	# 4. Именем для zip-архива служит текущая дата и время.
	target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
	# 5. Используем команду "zip" для помещения файлов в zip-архив
	zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
	# Запускаем создание резервной копии
	if os.system(zip_command) == 0:
		print('Резервная копия успешно создана в', target)
	else:
		print('Создание резервной копии НЕ УДАЛОСЬ')