import unittest
import random
from .sort import Sort

class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        print("Test Bubble Sort")
        array = random.sample(range(-100,100), 100)
        self.assertEqual(Sort.bubble_sort(array) ,sorted(array))

    def test_selection_sort(self):
        print("Test Selection Sort")
        array = random.sample(range(-100,100), 100)
        self.assertEqual(Sort.selection_sort(array) ,sorted(array))

    def test_insertion_sort(self):
        print("Test Insertion Sort")
        array = random.sample(range(-100,100), 100)
        self.assertEqual(Sort.insertion_sort(array) ,sorted(array))

    def test_merge_sort(self):
        print("Test Merge Sort")
        array = random.sample(range(-100,100), 100)
        self.assertEqual(Sort.merge_sort(array) ,sorted(array))

    def test_quick_sort(self):
        print("Test Quick Sort")
        array = random.sample(range(-100,100), 100)
        self.assertEqual(Sort.quick_sort(array) ,sorted(array))

    
if __name__ == "__main__":
    unittest.main()