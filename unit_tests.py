import random
import unittest
from BinarySearch import binary_search
from MergeSort import merge_sort
from QuickSort import quick_sort
from SelectionSort import selection_sort

test_list = [int(1000*random.random()) for i in xrange(100)]
sorted_list = sorted(test_list)

class BinarySearchCase(unittest.TestCase):
    def test_binary_search(self):
        foo = [1,32,56,84,97,105,325,725]
        self.assertEqual(binary_search(foo, 32), True)
        
class MergeSortCase(unittest.TestCase):
	def test_merge_sort(self):
		foo = list(test_list)
		merge_sort(foo)
		self.assertEqual(foo, sorted_list)

class QuickSortCase(unittest.TestCase):
	def test_quick_sort(self):
		foo = list(test_list)
		foo = quick_sort(foo)
		self.assertEqual(foo, sorted_list)

class SelectionSort(unittest.TestCase):
	def test_selection_sort(self):
		foo = list(test_list)
		self.assertEqual(selection_sort(foo), sorted_list)
		
if __name__ == '__main__':
    unittest.main()