def merge_sort(arr):
    if len(arr) > 1:   
        mid = len(arr) / 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = 0
        j = 0
        for k, v in enumerate(arr):
            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                continue
            if i < len(left):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
        return arr

def quick_sort(arr, begin = None, end = None):
    if begin is None and end is None:
        begin = 0
        end = len(arr)
    if end - begin <= 1:     
        pivot = arr[0]
        swap = begin - 1
        for indx, val in enumerate(arr[begin+1:end], 1):
            if val < pivot:
                swap += 1
                arr[indx], arr[swap] = arr[swap], arr[indx]
        arr[0], arr[swap] = arr[swap], arr[0]
        quick_sort(arr, begin = begin, end = swap)
        quick_sort(arr, begin = swap, end = end)
    return arr

if __name__ == "__main__":
    from timeit import Timer
    test = [10,5,20,2,25,29,50,17,60,51]
    t = Timer(lambda: merge_sort(test))
    print t.timeit(number=1)
                