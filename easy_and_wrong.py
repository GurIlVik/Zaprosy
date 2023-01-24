# JSON формат

# Формат сочетает в себе черты списков и словарей
# Ключами словаря могут быть только букво-числовые комбинации, начинающиеся с буквы
# https://www.json.org/json-ru.html


def save_str(data, filename):
    with open(filename) as f:
        f.write(data)


def format_json(data):
    return str(data).replace("'", '"')
# "\"" '\''
    

def load_json(filename):
    return parse_json(open(filename).read())


def parse_json(data):
    return eval(data)

# eval - вычислить
# exec - выполнить
# eval('b = 10') # ошибка! не выражение!
exec('b = 10')
print(b)



mydict = {
    "one": 1,
    "two": 2
}


json_string = format_json(mydict)

print(json_string)
print(type(json_string))
# print(json_string["two"])

new_dict = parse_json(json_string)
print(new_dict)


print(new_dict["two"])



