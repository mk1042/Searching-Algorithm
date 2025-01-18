
# Combined Search Algorithms: Binary Search and Linear Search

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Target not found


if __name__ == "__main__":
    # Example array and target
    array = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7

    # Binary Search requires sorted input
    print("Using Binary Search:")
    binary_result = binary_search(array, target)
    if binary_result != -1:
        print(f"Target {target} found at index {binary_result} using Binary Search.")
    else:
        print(f"Target {target} not found using Binary Search.")

    print("\nUsing Linear Search:")
    linear_result = linear_search(array, target)
    if linear_result != -1:
        print(f"Target {target} found at index {linear_result} using Linear Search.")
    else:
        print(f"Target {target} not found using Linear Search.")
