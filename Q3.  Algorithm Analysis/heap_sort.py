def Heap(array, length, index):
    n_if_statements = 0
    larger_index = index
    l_child = 2 * larger_index + 1
    r_child = 2 * larger_index + 2

    if l_child < length and array[larger_index] < array[l_child]:
        larger_index = l_child

    if r_child < length and array[larger_index] < array[r_child]:
        larger_index = r_child

    if larger_index != index:
        array[index], array[larger_index] = array[larger_index], array[index]

        n_if_statements += Heap(array, length, larger_index)

    n_if_statements += 2

    return n_if_statements

def heapSort(lyst, array_size):
    n_if_statements = 0
    #(1) Build a heap based on the elements in array[ ];
    for i in range(array_size-1, -1, -1):
        n_if_statements += Heap(lyst, array_size, i)
    #(2) for i = n-1 down to 1
    for i in range(array_size-1, 0, -1):
        #swap the element at root with the element in position i;
        lyst[i], lyst[0] = lyst[0], lyst[i]
        #restore the heap property for sub-array[0, …, i-1];
        n_if_statements += Heap(lyst, i, 0)

    return n_if_statements
