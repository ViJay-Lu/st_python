import unittest
from Chapter_11_testcode.full_name_test.name_function import *


class TestNameFunction(unittest.TestCase):
    def test_full_name(self):
        full_name = get_full_name('lu','vijay')
        self.assertEqual(full_name, 'Lu Vijay')

    def test_full_name_by_age(self):
        full_name = get_full_name_by_age('lu','vijay',32)
        self.assertEqual(full_name, 'lu vijay 32 years old')
#书中的写法为
# unittest.main()
#这样会报错。AttributeError: module '__main__' has no attribute 'test_name_function'

if __name__ == '__main__':
    unittest.main()
