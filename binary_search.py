def binary_search(input_arrray, search_value):
    low = 0
    high = len(input_arrray) - 1
    while low <= high:
        mid = (low + high) / 2
        if input_arrray[mid] == search_value:
            return mid
        elif input_arrray[mid] < search_value:
            low = mid + 1
        else:
            high = mid + 1
    return -1
