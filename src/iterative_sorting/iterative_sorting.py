# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for y in range(i, len(arr)):
            if arr[y] < arr[smallest_index]:
                smallest_index = y
        # TO-DO: swap
        # Your code here
        old_value = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = old_value

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                old_value = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = old_value
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
