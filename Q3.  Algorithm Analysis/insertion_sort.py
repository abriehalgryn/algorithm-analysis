def insertionSort(array, array_size):
    n_if_statements = 0
    i=1                               # starting point to be inserted

    while i<array_size:
        n_if_statements += 1                # Do n-1 insertion
        itemToInsert = array[i]
        j=i-1
        while j>=0:
            n_if_statements += 1
            # start search
            if itemToInsert <array[j]:
                array[j+1] = array[j]   #Shift right
                j -= 1
            else:
                break                 # found a index to insert
        array[j+1]= itemToInsert       # insert
        i += 1

    return n_if_statements
