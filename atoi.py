import unittest

def atoi(val, base):
    if val == 0:
        return str(0)
    current = val
    converted = list()
    while current > 0:
        remainder = current % base
        converted.append(remainder)
        if remainder > 0:
            current = (current - remainder) / base
        else:
            current = current / base
    return ''.join([str(x) for x in reversed(converted)])

class TestATOI(unittest.TestCase):
    def test_binary(self):
        for i in range(100):
            self.assertEqual(atoi(i, 2), bin(i)[2:])

if __name__ == '__main__':
    unittest.main()