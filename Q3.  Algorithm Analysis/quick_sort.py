def quickSort(lyst, array_size):
    n_if_statements = quicksortHelper(lyst, 0, array_size - 1)
    return n_if_statements

def quicksortHelper(lyst, left, right):
    n_if_statements = 0
    if left < right:
        pivotLocation, n_if_statements = partition(lyst, left, right)
        n_if_statements += quicksortHelper(lyst, left, pivotLocation - 1)
        n_if_statements += quicksortHelper(lyst, pivotLocation + 1, right)
    return n_if_statements + 1

def partition(lyst, left, right):
    n_if_statements = 0
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        n_if_statements += 1
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary)
    return boundary, n_if_statements

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
