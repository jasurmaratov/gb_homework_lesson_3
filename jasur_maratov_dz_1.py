num_list = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четире',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
}
def num_translate(num_world):
    return num_list.get(num_world)

def num_transtalen(num_world):
    to_key = num_list.get(num_world.lower())

    if to_key:
        return to_key.capitalize() if num_world[0].isupper() else to_key

    return None