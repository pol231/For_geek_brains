def int_func():
    """Пишет введенные слова с заглавной буквы"""
    for words in input('Введите слова на английском через пробел: ').split():
        if words.lower() == 'q':
            return 'Программа завершена'
        else:
            print(words.title())
    return int_func()
print(int_func())