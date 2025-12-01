def sequential_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

if __name__ == "__main__":
    data = [34, 7, 23, 32, 5, 62]
    target = 23

    print("Data:", data)
    print("Target to find:", target)
    
    seq_index = sequential_search(data, target)
    print(f"Sequential Search: Target {target} found at index {seq_index}")

    bin_index = binary_search(data, target)
    print(f"Binary Search: Target {target} found at index {bin_index}")