def max_element_iter(arr):
    max_val = arr[0]
    for x in arr[1:]:
        if x > max_val:
            max_val = x
    return max_val


def max_element_rec(arr):
    if len(arr) == 1:
        return arr[0]
    rest_max = max_element_rec(arr[1:])
    return arr[0] if arr[0] > rest_max else rest_max
