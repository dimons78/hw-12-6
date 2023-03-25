import unittest
from api_yandex import create_folder



class Test_Geo_logs(unittest.TestCase):

    def test_create_folder(self):
        self.assertEqual(create_folder('folder_12'), 201)




if __name__ == '__main__':
    unittest.main()
