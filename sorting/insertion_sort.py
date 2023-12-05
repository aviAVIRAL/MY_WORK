def insertion_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

# Example Usage
arr = [4, 65, 6, 33, 2, 3, 1]
insertion_sort(arr)
print(arr)
