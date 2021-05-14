def generalCountingSort(array, array_size):
    #create a empty list to add the sorted values in
    empty_list = [None for x in range(array_size)]


    #for each element of arr
    #set a current number
    for i in range(array_size):
        current_number = array[i]
        count = 0

        #this will count the total number of elements that are less than the current number
        #add 1 to count for each number that is less than it to determine its final position
        for j in range(array_size):
            if array[j] < current_number:
                count += 1

        #add the current number to its correct place in the new empty list
        #this loop will check if there is a number at the current count spot and if so move it up
        while empty_list[count] == current_number:
            count += 1
        empty_list[count] = current_number

    #this will return the newly sorted array
    return empty_list




# Below line read inputs from user using map() function
print("\nThese values have to be seperated by a space, e.g. 10 22 33 55 44")
arr = list(map(int,input("Enter the numbers : ").strip().split()))

#get the length of the user input array.
n = len(arr)
#This line will call the countingSort function, enter the list + listsize into the function
print(generalCountingSort(arr, n))
input("")
