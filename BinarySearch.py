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

def binary_search(arr, val):
    low = 0
    high = len(arr) - 1
    mid = (high + low) / 2
    found = False
    while low <= high and not found:
        if arr[mid] == val:
            found = True
        else:
            if arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1
            mid = (high + low) / 2
    return found
        