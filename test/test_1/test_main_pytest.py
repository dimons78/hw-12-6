import pytest
from geo_logs import get_geo_logs_Russia
from reo_id import get_list_unique
from res_Y import get_elem




class Test_Geo_logs:

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

    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}


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



    # def setup(self):
    #     print("method setup")
    #
    # def teardown(self):
    #     print("method teardown")


    def test_length(self):
        assert len(get_geo_logs_Russia(self.geo_logs)) == 6

    def test_length_ids(self):
        assert len(get_list_unique(self.ids)) == 6

    # Параметризация:
    # def test_length_elem1(self):
    #     assert len(get_elem(self.stats)) == 6
    #
    # def test_length_elem2(self):
    #     assert len(get_elem(self.stats2)) == 2
    #
    # def test_length_elem3(self):
    #     assert len(get_elem(self.stats3)) == 4

    # Параметризация:
    @pytest.mark.parametrize(
        "dict_in, len_out", (
        (stats, 6), (stats2, 2), (stats3, 4)
        )
    )
    def test_length_elem(self, dict_in, len_out):
        assert len(get_elem(dict_in)) == len_out


if __name__ == '__main__':
    pytest.main()

