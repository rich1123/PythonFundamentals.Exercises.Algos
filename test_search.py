import unittest
from search import binary_search
from unittest.mock import patch, call


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.list_in1 = [1, 2, 3, 4, 5]
        self.list_in2 = [1, 2, 3, 4, 5, 6, 7]
        self.list_in3 = [1, 2, 3, 4, 5, 6]
        self.item1 = 1
        self.item2 = 12
        self.item3 = -1

    def test_binary_search(self):
        self.assertEqual(binary_search(self.list_in1, self.item2), None)
        self.assertEqual(binary_search(self.list_in1, self.item3), None)
        self.assertEqual(binary_search(self.list_in2, self.item1), 0)

        # binary_search([1, 2, 3, 4, 5], 1)
        # binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 12)
        # binary_search([1, 2, 3, 4, 5, 6, 7, ], -1)

    # def test_search_again(self):
    #     with unittest.mock.patch('builtins.print') as mocked_print:

    @patch('builtins.print')
    def test_print(self, mocked_print):
        print('foo')
        print()
        assert mocked_print.mock_calls == [call('foo'), call()]
