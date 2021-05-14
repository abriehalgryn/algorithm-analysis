def countingSort(array, array_size):
    n_if_statements = 0
    empty_list = [None for x in range(array_size)]
    

    #for each element of arr
    #set a current number
    for i in range(array_size):
        current_number = array[i]
        count = 0

        #this will count the total number of elements that are less than the current number
        #add 1 to count for each number that is less than it to determine its final position
        for j in range(array_size):
            n_if_statements += 1
            if array[j] < current_number:
                count += 1

        #add the current number to its correct place in the new empty list
        empty_list[count] = current_number

    #this will display the newly sorted array)

    return n_if_statements
