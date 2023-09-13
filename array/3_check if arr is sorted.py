# check arr is sorted in asending oder(1->2->3 chote se bada)

def sorted_or_not(arr):
    n = len(arr)
    for i in range(1, n - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True

arr = [12, 3, 45, 67, 4, 58, 83]
print("Original array:", arr)
ans = sorted_or_not(arr)
print("Sorted or not:", ans)

arr = [1, 2, 3]
print("Original array:", arr)
ans = sorted_or_not(arr)
print("Sorted or not:", ans)
