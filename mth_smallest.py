#https://www.youtube.com/watch?v=D35llNtkCps
# get mth smallest integer

#average O(n)
# worst case O(n^2)
def mth_order_statistic(arr, m, begin=None, end=None):
  begin = 0 if begin is None else begin
  end = len(arr) if end is None else end

  pivot = begin
  switch = begin

  for i in range(begin+1, end):
    if arr[i] < arr[pivot]:
      switch += 1
      arr[switch], arr[i] = arr[i], arr[switch]
  arr[pivot], arr[switch] = arr[switch], arr[pivot]
  if switch == m - 1:
    return arr[switch]
  elif switch < m - 1:
    return mth_order_statistic(arr, m, switch+1, end)
  else:
    return mth_order_statistic(arr, m, begin, switch)

test_case = [3,2,5,6,10,21,15]

print(mth_order_statistic(test_case, 5))
