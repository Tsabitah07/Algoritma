# Selection Sort Implementation
def selection_sort_min(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def selection_sort_max(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        max_idx = i
        for j in range(i):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr



# Bubble Sort Implementation
def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n-i):
            if arr[j-1] < arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr



# Insertion Sort Implementation
def insertion_sort_asc(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



list_data = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", list_data)
print("Selection Sort (Min to Max):", selection_sort_min(list_data.copy()))
print("Selection Sort (Max to Min):", selection_sort_max(list_data.copy()))
print("Bubble Sort (Ascending):", bubble_sort_asc(list_data.copy()))
print("Bubble Sort (Descending):", bubble_sort_desc(list_data.copy()))
print("Insertion Sort (Ascending):", insertion_sort_asc(list_data.copy()))
print("Insertion Sort (Descending):", insertion_sort_desc(list_data.copy()))