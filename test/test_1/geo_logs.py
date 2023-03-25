# Дан список с визитами по городам и странам.
# Напишите код, который возвращает отфильтрованный список geo_logs,
# содержащий только визиты из России."


def get_geo_logs_Russia(list_):
    geo_logs_Russia = []
    for i in range(len(geo_logs)):
        # print(geo_logs[i].values())
        for j in geo_logs[i].values():
            # print(j)
            # print('Россия' in j)
            if 'Россия' in j:
                geo_logs_Russia.append(geo_logs[i])

    return geo_logs_Russia




geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

res = get_geo_logs_Russia(geo_logs)
print(res)
