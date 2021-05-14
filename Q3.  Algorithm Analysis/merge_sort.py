def merge_sort(array, array_size):
        # array            list to be sorted
        # buffer      temporary space needed during merge
    buffer = [None] * array_size
    n_if_statements = 0

    return merge_sort_helper(
        array,
        buffer,
        0, array_size-1,
        n_if_statements
    )


def merge_sort_helper(array, buffer, low, high, n_if_statements):
        # array            list to be sorted
        # buffer      temporary space needed during merge
        # high, low      bounds of sublist
        # middle          midpoint of sublist
    if low < high:
        n_if_statements += 1
        middle = (low + high) // 2
        #  print ("low, middle, high = ", low, middle, high)

        n_if_statements = merge_sort_helper(
            array, buffer, low, middle, n_if_statements
        )

        n_if_statements = merge_sort_helper(
            array, buffer, middle + 1, high, n_if_statements
        )
        #    print ("lyst - copyBuffer =>", lyst, "===", copyBuffer)

        n_if_statements += merge(array, buffer, low, middle, high)

    return n_if_statements

def merge(array, buffer, low, middle, high):
    n_if_statements = 0

    #initialize left_idx and right_idx to the 1st items in each sublist
    left_idx = low
    right_idx = middle + 1

    #interleave  items from the sublists into the
    #buffer in such a way that order is maintained.
    for i in range(low, high + 1):
        if left_idx > middle:
            n_if_statements += 1

            buffer[i] = array[right_idx] # 1st sublist exhausted
            right_idx += 1

        elif right_idx > high:
            n_if_statements += 2

            buffer[i] = array[left_idx]# 2nd sublist exhausted
            left_idx += 1

        elif array[left_idx] < array[right_idx]:# item in 1st sublist
            n_if_statements += 3

            buffer[i] = array[left_idx]
            left_idx += 1

        else:
            n_if_statements += 3

            buffer[i] = array[right_idx] # item in 2nd sublist
            right_idx += 1

    for i in range(low, high + 1):           # copy sorted items back to
        array[i] = buffer[i]     # proer position in array


    return n_if_statements
