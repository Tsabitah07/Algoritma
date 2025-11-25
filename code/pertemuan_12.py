# python
from typing import List, Tuple

def sequence_search(arr: List[int], target: int) -> int:
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

def min_max_pairwise(arr: List[int]) -> Tuple[int, int, int]:
    if not arr:
        raise ValueError("array must not be empty")
    n = len(arr)
    cmp_count = 0
    if n % 2 == 1:
        current_min = current_max = arr[0]
        i = 1
    else:
        cmp_count += 1
        if arr[0] < arr[1]:
            current_min, current_max = arr[0], arr[1]
        else:
            current_min, current_max = arr[1], arr[0]
        i = 2
    while i + 1 < n:
        cmp_count += 1
        if arr[i] < arr[i+1]:
            local_min, local_max = arr[i], arr[i+1]
        else:
            local_min, local_max = arr[i+1], arr[i]
        cmp_count += 1
        if local_min < current_min:
            current_min = local_min
        cmp_count += 1
        if local_max > current_max:
            current_max = local_max
        i += 2
    if i < n:  # odd leftover
        cmp_count += 1
        if arr[i] < current_min:
            current_min = arr[i]
        cmp_count += 1
        if arr[i] > current_max:
            current_max = arr[i]
    return current_min, current_max, cmp_count

if __name__ == "__main__":
    arr = [4, -4, 9, 7]
    print("array:", arr)
    idx = sequence_search(arr, 9)
    print("sequence_search(arr, 9) ->", idx)
    mn, mx, comps = min_max_pairwise(arr)
    print("min_max_pairwise -> min:", mn, "max:", mx, "comparisons:", comps)