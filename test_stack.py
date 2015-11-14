import unittest

class Test_Stack(unittest.TestCase):
    def test_push(self):
        test_stack = Stack()
        test_stack.push(5)
        test_stack.push(6)
        self.assertEqual(str(test_stack), '5 6')
        
class Stack(object):
    def __init__(self):
        self.data = []
    def __str__(self):
        return ' '.join([str(x) for x in self.data])
    def isempty(self):
        return not self.data
    def push(self, val):
        self.data.append(val)
    def pop(self):
        val = self.data[-1]
        self.data = self.data[:-1]
        return val
    
if __name__ == '__main__':
    unittest.main()