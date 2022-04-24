while True:
    number = int(input('Please enter any positive integer'))
    max_digit = 0
    number_int = number
    while number_int > 0:
        digit = number_int % 10
        if digit > max_digit:
            max_digit = digit
        number_int = number_int // 10
    break
print(f'The largest digit in a number is: {max_digit}')