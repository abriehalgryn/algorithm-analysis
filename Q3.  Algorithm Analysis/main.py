# this will import all the neccecary modules and functions to make the program work
import time
import os
from utils import getRandomArray
from utils import random_array
from utils import functionDetails
from merge_sort import merge_sort
from bubble_sort import bubbleSort
from selection_sort import selectionSort
from insertion_sort import insertionSort
from quick_sort import quickSort
from heap_sort import heapSort
from optimised_bubble_sort import optimalBubbleSort
from counting_sort import countingSort
from general_counting_sort import generalCountingSort
from table_print import print_table

# list of all the sorting algorithms
sort_names = [
    "Selection Sort",
    "Insertion Sort",
    "Merge Sort",
    "Quick Sort",
    "Heap Sort",
    "Bubble Sort",
    "Optimal Bubble Sort",
    "Counting Sort",
    "General Counting Sort"
    ]

# dictionary of all the sorting algorithms. This includees the name and the sort function call
sort_functions = {
    "Selection Sort": selectionSort,
    "Insertion Sort": insertionSort,
    "Merge Sort": merge_sort,
    "Quick Sort": quickSort,
    "Heap Sort": heapSort,
    "Bubble Sort": bubbleSort,
    "Optimal Bubble Sort": optimalBubbleSort,
    "Counting Sort": countingSort,
    "General Counting Sort": generalCountingSort
    }

# dictionary of array sizes to print the tables for question 3
array_sizes = {
    "100": None,
    "200": None,
    "400": None,
    "800": None,
    "1000": None,
    "2000": None
    }

# loop to keep the program running
loop = True
while loop:
    # main menu options print
    print("Welcome to the algorithm testing program \nWhat would you like to do?\n")
    print(
    "1. Test an individual sorting algorithm\n2. Test multiple sorting algorithms\n3. Experimental study: Average number of comparisons for sorting arrays (over 10 runs)\n4. Experimental study: Average running time (in ms) for sorting arrays of n integers (over 10 runs)\n5. Exit program\n")

    # this will go into a if statement to decide what code to run for the rest of the program
    choice = input("Please select (1), (2), (3), (4), (5): ")


    if choice in ["1", "individual", "Test an individual sorting algorithm"]:

        # calls the function getRandomArray to set a random array of input size to use for this option
        array = getRandomArray()
        # sets the array_size using the len() function
        array_size = len(array)


        # uses the sort_functions dictionary to print out the menu for which algorithm to singulary test
        count = 1
        for sort_name, sort in sort_functions.items():
            print(str(count) + ".", sort_name)
            # increments 1 to print neatly
            count += 1

            # loop to keep the program running (for error checking)
            # uses try except to make sure the input is correct
        while True:
            try:
                test = int(input("Which algorithm would you like to test? "))
                sort_name = sort_names[test-1]
                #break out of loop when correct input is inserted
                break
            except:
                print("This is not a int!")


        # runs code based on function which depends on user input "test"
        if test == 1:
            functionDetails(selectionSort, array, array_size, sort_name)

        elif test == 2:
            functionDetails(insertionSort, array, array_size, sort_name)

        elif test == 3:
            functionDetails(merge_sort, array, array_size, sort_name)

        elif test == 4:
            functionDetails(quickSort, array, array_size, sort_name)

        elif test == 5:
            functionDetails(heapSort, array, array_size, sort_name)

        elif test == 6:
            functionDetails(bubbleSort, array, array_size, sort_name)

        elif test == 7:
            functionDetails(optimalBubbleSort, array, array_size, sort_name)

        elif test == 8:
            functionDetails(countingSort, array, array_size, sort_name)

        elif test == 9:
            functionDetails(generalCountingSort, array, array_size, sort_name)

        else:
            # error checking
            print("Invalid input")


    elif choice in ["2"]:

        # calls the function getRandomArray to set a random array of input size to use for this option
        generate_array = getRandomArray()
        array_size = len(generate_array)

        # empty table data to be appended to for neat tabble formatting
        table_data = []

        #loop that runs for the sort_functions dictionary
        for sort_name, sort in sort_functions.items():
            # uses .copy() so that each array that the sorting algorithms sort are the same for best results
            # time is used to calculate how long a algorithm took
            array = generate_array.copy()
            start_time = time.time()
            n_if_statements = sort(array, array_size)
            elapsed_time = time.time() - start_time
            formatted_time = str(round(elapsed_time*1000, 2))+ " ms"
            # this sends the data to the table, which will neatly display it
            table_data.append({"Sorting Algorithm": sort_name, "Array Size": array_size, "Num. Comparisons": n_if_statements, "Run Time": formatted_time})

        # neatly prints the table using the print+table function
        print_table(table_data, alignments=["l", "r", "r", "r"])



    elif choice in ["3"]:
        # empty table data to be appended to for neat tabble formatting
        table_data = []
        #loop that runs for the sort_functions dictionary
        for sort_name, sort in sort_functions.items():
            #loop that runs for the array_sizes dictionary
            for array_size in array_sizes:
                n_if_statements = 0
                # loop that runs 10 times to get the average
                for i in range(10):
                    array = random_array(int(array_size))
                    n_if_statements += sort(array, int(array_size))
                    # gets the average
                array_sizes[array_size] = n_if_statements / 10

            # this sends the data to the table, which will neatly display it
            table_data.append({"Sorting Algorithm": sort_name, **array_sizes})

        # neatly prints the table using the print+table function
        print_table(table_data, alignments=["l", "r", "r", "r", "r", "r", "r"])


    elif choice in ["4"]:
        # empty table data to be appended to for neat tabble formatting
        table_data = []

        #loop that runs for the sort_functions dictionary
        for sort_name, sort in sort_functions.items():
            #loop that runs for the array_sizes dictionary
            for array_size in array_sizes:
                n_if_statements = 0
                timer = 0
                # loop that runs 10 times to get the average time
                for i in range(10):
                    array = random_array(int(array_size))
                    start_time = time.time()
                    n_if_statements += sort(array, int(array_size))
                    elapsed_time = time.time() - start_time
                    timer += elapsed_time
                # get the average time
                timer /= 10
                # formatting for ms at the end of the time
                # timesed by 1000 to makes sure that the answer is in ms
                formatted_time = str(round(timer*1000, 2))+ " ms"
                array_sizes[array_size] = formatted_time

                # this sends the data to the table, which will neatly display it
            table_data.append({"Sorting Algorithm": sort_name, **array_sizes})

            # neatly prints the table using the print+table function
        print_table(table_data, alignments=["l", "r", "r", "r", "r", "r", "r"])



    elif choice in ["5"]:
        loop = False


    else:
        print("Invalid Input")


    input("Press Enter to continue")
    os.system('cls')
