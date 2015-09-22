def selection_sort(arr):
	for i in range(len(arr)):
		max = 0
		for j in range(len(arr)-i):
			if arr[j] > arr[max]:
				max = j
		tmp = arr[len(arr)-1-i]
		arr[len(arr)-1-i] = arr[max]
		arr[max] = tmp
	return arr