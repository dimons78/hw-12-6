# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т.е. в данном примере скрипт должен возвращать 'yandex'.

def get_elem(dict_):
    max_elem = 0
    id_elem = None

    for key in dict_:
        # print(key)
        if dict_[key] > max_elem:
            max_elem = dict_[key]
            id_elem = key

    return id_elem


stats = {'facebook': 55,
         'yandex': 120,
         'vk': 115,
         'google': 99,
         'email': 42,
         'ok': 98}
