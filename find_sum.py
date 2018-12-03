#https://www.youtube.com/watch?v=XKu_SEDAykw
def find_sum_sorted(arr, val, begin=None, end=None):
  if begin is None:
    begin = 0
  if end is None:
    end = len(arr) - 1
  if end <= begin:
    return None
  candidate_sum = arr[begin] + arr[end]
  print(arr[begin], arr[end], candidate_sum)
  if candidate_sum == val:
    return begin, end
  elif candidate_sum > val:
    end -= 1
  else:
    begin += 1
  return find_sum(arr, val, begin, end)

def find_sum(arr, val, bitmap=None):
  if bitmap is None:
    bitmap = set()
  for i in arr:
    complement = val - i
    if complement in bitmap:
      return True
    else:
      bitmap.add(i)
  return False
    

import random
test_case = [51, 8, 35, 12, 34, 34, 52]
print(find_sum(test_case, 44))
