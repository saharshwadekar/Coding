import random

def modified_binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if (arr[low] <= arr[mid] and arr[low] <= target < arr[mid]) or \
           (arr[mid] < arr[high] and arr[mid] < target <= arr[high]):
            high = mid - 1
        else:
            low = mid + 1

    return -1

size = 10
min_val, max_val = 0, 100

arr = sorted(random.randint(min_val, max_val) for _ in range(size))

print("Generated list:", arr)
target = int(input("Target to be searched: "))

index = modified_binary_search(arr, target)
if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found in the list.")