def binary_search_recursive(arr, val):
    mid = len(arr) / 2
    status = "not found"
    if arr[mid] == val:
        return "found"
    else:
        if len(arr) != 1:
            if arr[mid] < val:
                status = binary_search(arr[mid:], val)
            elif arr[mid] > val:
                status = binary_search(arr[:mid], val)
    return status

# def binary_search(arr, val):
#     low = 0
#     high = len(arr) - 1
#     mid = (high + low) / 2
#     found = False
#     while low <= high and not found:
#         if arr[mid] == val:
#             found = True
#         else:
#             if arr[mid] < val:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#             mid = (high + low) / 2
#     return found

def binary_search(arr, val):
    found = False
    i = 0
    j = len(arr)
    while i <= j:
        mid = (i + j) / 2
        if val == arr[mid]:
            return 'found'
        elif val < arr[mid]:
            j = mid
        else:
            i = mid + 1
    return 'not found'
        
    
def binary_search_in_place(arr, val, begin=None, end=None):
    if begin == None:
        begin = 0
    if end == None:
        end = len(arr) - 1
    found_index = -1
    if end - begin > -1:
        mid = begin + int((end - begin) / 2)
        if val == arr[mid]:
          found_index = mid
        elif val < arr[mid]:
          found_index = binary_search_in_place(arr, val, begin, mid-1)
        else:
          found_index = binary_search_in_place(arr, val, mid+1, end)
    if found_index > -1:
        return found_index
    return -1




def binary_search_ceil(arr, val):
  if not arr:
    return None
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = int((high + low) / 2)
    print(low, mid, high)
    if arr[mid] == val:
      return arr[mid]
    elif arr[mid] < val:
      low = mid + 1
    else:
      high = mid - 1
  if low == len(arr):
    low -= 1
  return arr[low]


def binary_search_floor(arr, val):
  if not arr:
    return None
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = int((high + low) / 2)
    print("before", low, mid, high)
    if arr[mid] == val:
      return arr[mid]
    elif arr[mid] < val:
      low = mid + 1
    else:
      high = mid - 1
  print(low, mid, high)
  if high == -1:
    high = 0
  return arr[high]


foo = binary_search_floor([2,4,6], 7)

print(foo)
