from return_data_file import data_file

def copy_data():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row> count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    copy_data_list=data[count_rows-1]
    data, nf = data_file()        
    now_number_row = len(data) + 1
    copy_data_list = copy_data_list.replace(str(number_row ),str(now_number_row))
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{copy_data_list}\n')
    print("Данные успешно записаны!")