def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example Usage
arr = [4, 65, 6, 33, 2, 3, 1]
bubble_sort(arr)
print(arr)
