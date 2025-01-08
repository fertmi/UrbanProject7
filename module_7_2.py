def custom_write(file_name, strings):
    file = open (file_name, 'w', encoding= 'utf-8')
    number_line = 1
    byte_start_string = file.tell()
    strings_positions = {}
    for i in range(len(strings)):
        file.write(f'{strings[i]}\n')
        strings_positions[(number_line, byte_start_string)] = f'{strings[i]}'
        byte_start_string = file.tell()
        number_line += 1
    return strings_positions

#Основная программа
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
