# import neccecary modules
from random import sample
import time
from table_print import print_table

# creates a array of random characters that are all unique
def random_array(n, low=0, high=1000000):
    return sample(range(low, high), n)

# function to set a random array
def getRandomArray():
    # loop for error checking
    while True:
        try:
            array_size = int(input("Enter size of array you would like to test: "))
            random_arrays = random_array(array_size)
            return random_arrays
            break
        except:
            print("That is not a array size!")
            pass

# print details of a specific algorithm in a table
def functionDetails(sort_type, array, array_size, sort_name):
    # empty list of table formatting
    table_data = []

    # use time for timing the function
    start_time = time.time()
    n_if_statements = sort_type(array, array_size)
    elapsed_time = time.time() - start_time
    # formats the elapsed ttime to be in ms
    formatted_time = str(round(elapsed_time*1000, 2))+ " ms"
    # adds to the table data
    table_data.append({"Sorting Algorithm": sort_name, "Array Size": array_size, "Num. Comparisons": n_if_statements, "Run Time": formatted_time})
    # neatly prints the table
    print_table(table_data, alignments=["l", "r", "r", "r"])
