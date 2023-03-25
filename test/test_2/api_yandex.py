import requests
from pprint import pprint


host = 'https://cloud-api.yandex.net:443'
# Открываем ЯНДЕКС ТОКЕН
with open('D:/Учеба/Нетология 2022/Яндекс токен/Токен с Полигон.txt', encoding='utf-8') as file:
    TOKEN = file.readline().rstrip()


# создание папки на Я-диске
def create_folder(folder):
    url = f'{host}/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    params = {'path': folder}
    response = requests.put(url, headers=headers, params=params)
    # pprint(response.json())
    # print(response.status_code)
    res = response.status_code
    return res


# Создаем папку на Я-диске
create_folder('new_folder_3')
