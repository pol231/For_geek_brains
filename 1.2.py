all_sec = int(input('Please enter any number of seconds'))
hours = all_sec // 3600
minutes_modify = all_sec % 3600
minutes = minutes_modify // 60
seconds = all_sec % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')