def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr[0]
        i = 1
        for j in range(1, len(arr)):
            if arr[j] < pivot:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
                i += 1
            
        tmp = arr[i-1]
        arr[i-1] = pivot
        arr[0] = tmp
        
        left = quick_sort(arr[:i-1])
        left.append(pivot)
        right = quick_sort(arr[i:])
        arr = left + right
        return arr
    else:
        return arr

def quick_sort_in_place(arr, begin = None, end = None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(arr)
    length = end - begin
    if length > 1:
        pivot = arr[begin]
        i = begin + 1
        for j in range(begin+1, end):
            if arr[j] < pivot:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
                i += 1
        tmp = arr[i-1]
        arr[i-1] = pivot
        arr[begin] = tmp
        
        quick_sort_in_place(arr, begin=begin, end=i-1)
        quick_sort_in_place(arr, begin=i, end=end)
    return arr




        
    