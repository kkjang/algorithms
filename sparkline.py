# -*- coding: utf-8 -*-

import math
import unittest

ticks = [u'▁', u'▂', u'▃', u'▄', u'▅', u'▆', u'▇', u'█']



def sparkline(input_str):
    vals = [x for x in map(int, input_str.split())]
    max_val = max(vals)
    min_val = min(vals)
    val_range = max_val - min_val
    for i, val in enumerate(vals):
      tick_index = math.floor((val-min_val) * (len(ticks) / val_range))
      if tick_index == len(ticks):
        tick_index -= 1
      vals[i] = ticks[tick_index]
    return "".join(vals)
    

print sparkline("28 25 26 23 20 19")


class SparkLineTest(unittest.TestCase):
    def test_spark_line(self):
        self.assertEqual(sparkline("28 25 26 23 20 19"), u"█▆▇▄▁▁")

        
if __name__ == '__main__':
    unittest.main()
