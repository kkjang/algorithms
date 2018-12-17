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

def string_permutations_in_order(string_arr, prefix=""):
    if not string_arr:
        print(prefix)
    for i, val in enumerate(string_arr):
        new_prefix = prefix + val
        new_string_arr = string_arr[:i] + string_arr[i+1:]
        string_permutations_in_order(new_string_arr, new_prefix)

test_case = list('abcd')
string_permutations(test_case)
string_permutations_in_order(test_case)
