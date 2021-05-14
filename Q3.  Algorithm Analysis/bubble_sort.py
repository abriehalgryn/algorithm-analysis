def bubbleSort(array, array_size):
    n_if_statements = 0
    #This will iterate through each item of the array - 1 the last element as it does not have to be comapred as there is nothing to compare it to
    for i in range(array_size):
    #If the range is set to range(n), the outer loop will repeat more than needed.
  
        #The last i elements are already in place
        
        #This will loop  the array starting at the 0 and ending at n-1
        for j in range(array_size-1):

            #If it is found that they have to be swapped, the values of the array contents are switched accordingly:
            n_if_statements += 1
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]


    return n_if_statements
