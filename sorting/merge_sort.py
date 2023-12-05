def merge(arr, low, mid, high):
    temp = []  # Temporary array to hold merged elements
    left = low  # Starting index of left subarray
    right = mid + 1  # Starting index of right subarray

    # Merging sorted subarrays into temp
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Adding remaining elements from left subarray
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Adding remaining elements from right subarray
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copying merged elements back to original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)  # Sort left half
    merge_sort(arr, mid + 1, high)  # Sort right half
    merge(arr, low, mid, high)  # Merge sorted halves

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)

merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
