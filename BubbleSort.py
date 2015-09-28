def bubble_sort(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(len(arr)- i - 1):
            count += 1
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
    return arr, count

def short_bubble_sort(arr):
    count = 0
    for i in range(len(arr)-1):
        change = False
        for j in range(len(arr) - i - 1):
            count += 1
            if arr[j] > arr[j+1]:
                change = True
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
        if change == False:
            return arr, count
    return arr, count
                
# test = [2,3,4,5,1]
# print bubble_sort(list(test))
# print short_bubble_sort(list(test))

