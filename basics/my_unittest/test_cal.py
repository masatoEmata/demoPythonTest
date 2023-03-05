import unittest
from cal import Cal

release_name = 'lesson'

class CalTest(unittest.TestCase):
    def setUp(self) -> None:
        print('setup')
        self.cal = Cal()

    def tearDown(self) -> None:
        print('cleanup')
        del self.cal

    @unittest.skipIf(release_name == 'lesson', 'skip!')
    def test_add_num_and_double(self):
        self.assertEqual(
            self.cal.add_num_and_double(1, 1),
            4
        )

    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()