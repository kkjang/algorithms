def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) / 2
        left = arr[:m]
        right = arr[m:]
        merge_sort(left)
        merge_sort(right)
        
        i=0
        j=0
        for k in range(len(arr)):
            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
            elif (i < len(left)):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
        