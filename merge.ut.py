import unittest
from merge import merge_range
from merge import merge_range2

class TestMergeFunction(unittest.TestCase):

    def setUp(self):
        self.merge = merge_range

    def test_merge_range_valid_withsample1(self):
        result = merge_range([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        self.assertEqual(result, [(0, 1), (3, 8), (9, 12)])

    def test_merge_range2_valid_withsample1(self):
        result = merge_range2([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        self.assertEqual(result, [(0, 1), (3, 8), (9, 12)])

    def test_merge_range_valid_withsample2(self):
        result = merge_range([(1, 5), (6,7), (2, 3)])
        self.assertEqual(result, [(1, 5), (6, 7)])

    def test_merge_range2_valid_withsample2(self):
        result = merge_range2([(1, 5), (6,7), (2, 3)])
        self.assertEqual(result, [(1, 5), (6, 7)])
    
    def test_merge_range_valid_withsample3(self):
        result = merge_range([(1, 10), (2, 6), (3, 5), (7, 9)])
        self.assertEqual(result, [(1, 10)])
    
    def test_merge_range2_valid_withsample3(self):
        result = merge_range2([(1, 10), (2, 6), (3, 5), (7, 9)])
        self.assertEqual(result, [(1, 10)])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)