def custom_write(file_name, strings) :


    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as f :
        for i, string in enumerate(strings, 1) :
            start_pos = f.tell()
            f.write(string + '\n')
            strings_positions[(i, start_pos)] = string
    return strings_positions


if __name__ == '__main__' :
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items() :
    print(elem)
