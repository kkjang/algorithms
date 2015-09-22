import sys
import import_notebook
import random
import unittest
from BinarySearch import binary_search

test_list = [int(1000*random.random()) for i in xrange(100)]
sorted_list = sorted(test_list)

class BinarySearchCase(unittest.TestCase):
    def test_binary_search(self):
        foo = [1,32,56,84,97,105,325,725]
        self.assertEqual(binary_search(foo, 1), True)
        
        
suite = unittest.TestLoader().loadTestsFromTestCase(BinarySearchCase)
unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )
        
if __name__ == '__main__':
    unittest.main()