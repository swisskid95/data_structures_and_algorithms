def bubble_sort(input_array):
    n = len(input_array)
    # To keep track of the swaps during a single array traversal
    for i in range(n):
        num_of_swaps = 0
        for j in range(n - 1):
            # Swap adjacent elements if they are in decreasing order
            if input_array[j] > input_array[j + 1]:
                input_array[j], input_array[j +
                                            1] = input_array[j + 1], input_array[j]
                num_of_swaps += 1

        # If no elements were swapped during a traversal, array is sorted
        if num_of_swaps == 0:
            break
    return input_array
