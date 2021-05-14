def selectionSort(aList, array_size):
    n_if_statements = 0
    # Sort aList[ ] into ascending order.
    for i in range(array_size):
        least = i
        for k in range(i+1 , array_size):
            n_if_statements += 1
            if aList[k] < aList[least]:
                least = k
        swap( aList, least, i )

    return n_if_statements



#FROM WORKSHOP
def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
