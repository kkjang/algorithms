# -*- coding: utf-8 -*-

import math
import unittest

ticks = [u'▁', u'▂', u'▃', u'▄', u'▅', u'▆', u'▇', u'█']



def sparkline(input_str):
    foo = map(int, input_str.split())
    maximum = max(foo)
    minimum = min(foo)
    increments = (maximum - minimum) / float(len(foo))
    bar = (maximum - minimum) / 8.0
    graph = [None] * len(foo)
    for i in range(len(foo)):
        tick_index = math.ceil((foo[i] - minimum) / bar)
        if tick_index < 1:
            graph[i] = ticks[int(tick_index)]
        else:
            graph[i] = ticks[int(tick_index) - 1]
    return ''.join(graph)
    

print sparkline("12 30 1 2 6 24 16 23 27 9 15")


class SparkLineTest(unittest.TestCase):
    def test_spark_line(self):
        self.assertEqual(sparkline("28 25 26 23 20 19"), u"█▆▇▄▁▁")

        
if __name__ == '__main__':
    unittest.main()