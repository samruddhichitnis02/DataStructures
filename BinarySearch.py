import random

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

def binary_search(arr, num):
    
