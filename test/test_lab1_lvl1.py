import unittest
from src.lab_1.lab_1_lvl_1 import square_sorted_list
# print(square_sorted_list([1, 2, 3], [1, 2, 3, 4]))


class TestLab(unittest.TestCase):
    def test_subarray_true(self):
        result = square_sorted_list([-4, -2, 0, 1, 3])
        self.assertEqual(result, [0, 1, 4, 9, 16])


if __name__ == '__main__':
    unittest.main()
