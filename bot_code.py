import json
import random
import config
import os
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
    example_path = "data/example.json"
    with open(f'{example_path}', 'r') as f:
        parameters = json.load(f)
    parameters['name'] = name
    with open(f'{file_path}', "w") as file:
        json.dump(parameters, file, ensure_ascii=False, indent=2, sort_keys=True)
    msg = f', ты получаешь новый писюн, котрый будешь растить.'
    return msg


def check_new_member(name):
    file_path = f"data/{name}.json"
    if os.path.exists(file_path):
        print(parse_data(file_path))
    else:
        print(create_new_member(file_path, name))


# if __name__ == "__main__":
#     check_new_member('artem')
