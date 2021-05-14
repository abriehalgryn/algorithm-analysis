#Assignment 2: Algorithm Implementation and Analysis
#Abrie Halgryn
#Student number: 10496171


import time

#Question 1, 1(c):

# Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)

    #This will iterate through each item of the array - 1 the last element as it does not have to be comapred as there is nothing to compare it to
    for i in range(n-1):
    #If the range is set to range(n), the outer loop will repeat more than needed.

        #The last i elements are already in place

        #This will loop  the array starting at the 0 and ending at n-1
        for j in range(0, n-1):

            #If it is found that they have to be swapped, the values of the array contents are switched accordingly:
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]



# Question 1, 1(d):
# Python program for implementation of Bubble Sort
def optimalBubbleSort(arr):
    n = len(arr)

    #This will iterate through each item of the array - 1 the last element as it does not have to be comapred as there is nothing to compare it to
    for i in range(n-1):
    #If the range is set to range(n), the outer loop will repeat more than needed.

        #The last i elements are already in place

        #This will loop  the array starting at the 0 and ending at n-i-1 QUESTION 1(D)
        for j in range(0, n-i-1): #this removes i from n to avoid scanning the entire array over and over as i is the amount of elements that is already "bubbled up" so they cannot move more

            #If it is found that they have to be swapped, the values of the array contents are switched accordingly:
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]




# Below line read inputs from user using map() function
print("\nThese values have to be seperated by a space, e.g. 10 22 33 55 44")
arr = list(map(int,input("Enter the numbers : ").strip().split()))

#This line will call the bubble sort function, enter the list into the function
# START MY TIMER - will be used to calculate the amount of time the function takes to run
start_time = time.time()
bubbleSort(arr)
#optimalBubbleSort(arr)
elapsed_time = time.time() - start_time # in seconds, this value can be multiplied by 10 to give the answer in milliseconds

#This will print the sorted array
print ("Sorted array is:", arr)
print("Time Taken:", float(elapsed_time))
input(" ") #this line of code is here so that if its run in cmd the window doesnt instantly close


print("1. Print the pre-order of the BST")
print("2. Print the in-order of the BST")
print("3. Print the post-order of the BST")
print("4. Print all leaf nodes of the BST, and all non-leaf nodes (separately)")
print("5. Print the total number of nodes of a sub-tree")
print("6. Print the depth of a subtree rooted at a particular node")
print("7. Insert a new integer key into the BST")
print("8. Delete an integer key from the BST")
print("9. Exit")
