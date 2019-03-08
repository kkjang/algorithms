def max_product_k_numbers(arr, k):
  """
  Given an array and size k, find the subsequence of size k
  that gives the largest product
  
  """
  if not arr:
    return 0
  max_product = 0

  for index in range(0, k+1, 2):
    bottom = product(arr, range(index))
    top = product(arr, range(len(arr)-k+index, len(arr)))
    max_product = max(max_product, bottom*top)

  return max_product

def product(arr, arr_range):
  cur_product = 1
  for index in arr_range:
    cur_product *= arr[index]
  return cur_product

print(max_product_k_numbers([0], 1))
