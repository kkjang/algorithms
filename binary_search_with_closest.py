import math

# Also return closest if not found
def binary_search(arr, val, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(arr) - 1
    if begin >= end:
        return end
    mid = math.ceil((end - begin) / 2) + begin
    print(begin, mid, end)
    if arr[mid] == val:
        return mid
    elif arr[mid] > val:
        return binary_search(arr, val, begin, mid-1)
    else:
        return binary_search(arr, val, mid+1, end)

test_case = [3,5,7,9,11,13]
print(binary_search(test_case, 12))
