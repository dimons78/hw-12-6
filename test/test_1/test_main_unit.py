import unittest
from geo_logs import get_geo_logs_Russia
from reo_id import get_list_unique
from res_Y import get_elem


class Test_Geo_logs(unittest.TestCase):

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

    list_res = [
        {'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']},
         {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']},
         {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}
    ]

    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    res_ids = [98, 35, 15, 213, 54, 119]

    stats = {'facebook': 55,
             'yandex': 120,
             'vk': 115,
             'google': 99,
             'email': 42,
             'ok': 98}

    stats2 = {'facebook': 55,
             'yandex': 12,
             'vk': 115,
             'google': 99,
             'email': 42,
             'ok': 98,
             'visa': 11}

    stats3 = {'facebook': 55,
             'yandex': 120,
             'vk': 115,
             'google': 99,
             'email': 42,
             'ok': 98,
             'visa': 146}

    # def setUp(self):
    #     print("method setUp")
    #
    # def tearDown(self):
    #     print("method tearDown")

    def test_get_geo_logs_Russia(self):
        self.assertEqual(get_geo_logs_Russia(self.geo_logs), self.list_res)

    def test_get_list_unique(self):
        self.assertEqual(get_list_unique(self.ids), self.res_ids)

    # Параметризация:
    def test_get_elem_1(self):
        self.assertEqual(get_elem(self.stats), "yandex")

    def test_get_elem_2(self):
        self.assertEqual(get_elem(self.stats2), "vk")

    def test_get_elem_3(self):
        self.assertEqual(get_elem(self.stats3), "visa")


if __name__ == '__main__':
    unittest.main()
