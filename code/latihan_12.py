list = [25, 70, 10, 80, 5, 45, 15]

def devided_conquer_max_search(arr, left, right):
    if left == right:
        return arr[left], 0

    mid = (left + right) // 2

    max_left, comps_left = devided_conquer_max_search(arr, left, mid)
    max_right, comps_right = devided_conquer_max_search(arr, mid + 1, right)

    total_comps = comps_left + comps_right + 1

    if max_left > max_right:
        return max_left, total_comps
    else:
        return max_right, total_comps



def devided_conquer_min_search(arr, left, right):
    if left == right:
        return arr[left], 0

    mid = (left + right) // 2

    min_left, comps_left = devided_conquer_min_search(arr, left, mid)
    min_right, comps_right = devided_conquer_min_search(arr, mid + 1, right)

    total_comps = comps_left + comps_right + 1

    if min_left < min_right:
        return min_left, total_comps
    else:
        return min_right, total_comps



if __name__ == "__main__":
    print("\nList:", list)
    max_value, max_comps = devided_conquer_max_search(list, 0, len(list) - 1)
    min_value, min_comps = devided_conquer_min_search(list, 0, len(list) - 1)
    print("Max value:", max_value, "with comparisons:", max_comps)
    print("Min value:", min_value, "with comparisons:", min_comps)