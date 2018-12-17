def string_permutations(string_arr, begin=None):
    if begin is None:
        begin = 0
    if begin == len(string_arr)-1:
        print("".join(string_arr))
    for i in range(begin, len(string_arr)):
        if i != begin:
            string_arr[i], string_arr[begin] = string_arr[begin], string_arr[i]
        string_permutations(string_arr, begin+1)
        if i != begin:
            string_arr[i], string_arr[begin] = string_arr[begin], string_arr[i]

string_permutations(list("abcd"))
