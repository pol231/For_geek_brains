while True:
    start = int(input('Пожалуйста, введите начальный результат в км'))
    finish = int(input('Пожалуйста, введите конечный результат в км'))
    days = 1
    while start <= finish:
        start = start + start / 10
        days += 1
    print(f'Конечный резльтат будет получен на {days} день')
    break
