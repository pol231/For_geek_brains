def info(name, surname, year, city, email, mobile):
    return f'имя - {name}, фамилия - {surname}, год_рождения- {year}, город - {city}, почта - {email}, телефон -{mobile}'
print(info(name=input("Как вас зовут?: "), surname=input("Какая у вас фамилия?: "), year=input("Год вашего рождения?: "),
           city=input("Где вы живете?: "), email=input("Ваша почта?: "), mobile=input("Ваш номер телефона?: ")))