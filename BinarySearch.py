import random
random.seed("Hello")

numbers = [random.randint(0, 500) for i in range(100)]

print(numbers)
print()

# Step 1: Sort the list (Using bubble sort to sort the array)
def sort_arr(arr):
    n = len(arr) - 1

    for i in range(n * n):
        pos = i % n
        if arr[pos] > arr[pos + 1]:
            arr[pos], arr[pos + 1] = arr[pos + 1], arr[pos]

    return arr

def binary_search(arr, num, left, right):

    # sort the array first
    arr = sort_arr(arr)

    if left > right:
        return -1
    
    mid = (left + right) // 2
    if num == arr[mid]:
        return mid
    
    elif num < arr[mid]:
        return binary_search(arr, num, left, mid)

    else:
        return binary_search(arr, num, mid, right)
    
element_index = binary_search(numbers, 4, 0, len(numbers) - 1)
print(element_index)

# Note: This Binary Search Algorithm runs on Big O of logn