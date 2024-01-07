import json
import random
import config
import os
import base64
from datetime import date


def calc_length():
    result = random.randint(config.left_side, config.right_side)
    return result


def check_date(game_date):
    if game_date == str(date.today()):
        return True
    else:
        return False


def save_to_json(parameters, file_path):
    with open(f'{file_path}', "w") as file:
        json.dump(parameters, file, ensure_ascii=False, indent=2, sort_keys=True)


def parse_data(file_path):
    with open(f'{file_path}', 'r') as f:
        parameters = json.load(f)
    length = parameters['parameters']['length']
    game_date = parameters['parameters']['game_date']
    if check_date(game_date):
        msg = f', ты уже играл. Сейчас он равен {length} см. Следующая попытка завтра!'
        return msg
    else:
        game_date = str(date.today())
        add_length = calc_length()
        while add_length == 0:
            add_length = calc_length()

        length = int(length) + add_length
        parameters['parameters']['length'] = length
        parameters['parameters']['game_date'] = game_date
        save_to_json(parameters, file_path)
        if add_length > 0:
            msg = f', твой писюн вырос на {add_length} см. Теперь он равен {length} см.' \
                  f' Следующая попытка завтра!'
        else:
            msg = f', твой писюн стал меньше на {abs(add_length)} см. Теперь он равен {length} см.' \
                  f' Следующая попытка завтра!'
        return msg


def create_new_member(file_path, name):
    name = str(name)
    example_path = "data/example.json"
    with open(f'{example_path}', 'r') as f:
        parameters = json.load(f)
    parameters['name'] = str(name)
    with open(f'{file_path}', "w", encoding='utf-8') as file:
        json.dump(parameters, file, ensure_ascii=False, indent=2, sort_keys=True)
    msg = f', ты получаешь новый писюн, котрый будешь растить.'
    return msg


def check_new_member(id_tg, name, fullname):
    file_path = f"data/{id_tg}.json"
    name = fullname
    if os.path.exists(file_path):
        return parse_data(file_path)
    else:
        return create_new_member(file_path, name)


def files_list():
    directory = "data"
    # Получаем список файлов
    files = os.listdir(directory)
    files.remove('example.json')
    return files


def create_members_list(files):
    result = {}
    for file in files:
        with open(f'data/{file}', 'r', encoding='utf-8') as f:
            parameters = json.load(f)
        result[parameters['name']] = parameters['parameters']['length']
    return result


def check_top():
    files = files_list()
    member = create_members_list(files)
    sorted_member = sorted(member.items(), key=lambda item: item[1], reverse=True)
    msg = 'Топ игроков: \n'
    count = 1
    for i in sorted_member:
        msg += f'{count}) {i[0]} = {i[1]} см.\n'
        count += 1

    return msg


if __name__ == "__main__":
    print(check_top())