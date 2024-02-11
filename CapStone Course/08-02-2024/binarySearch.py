import random

def modified_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# Example usage
size = 10
min_val = 0
max_val = 100

arr = [random.randint(min_val, max_val) for _ in range(size)]
arr.sort()

print("Generated list:", arr)
target = int(input("Target to be search: "));

index = modified_binary_search(arr, target)
if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found in the list.")
