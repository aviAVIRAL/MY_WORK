

# find kr target {x}  elm ke index ko in arr 

# tc =     O(logN)               


def binarySearch(arr,  target):
    n = len(arr)  # size of the array
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target  :
            return mid    
        elif  arr[mid]  > target   :   
            high = mid - 1
        else:
            low = mid + 1

    return -1

if __name__ == "__main__":
    arr = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    ind = binarySearch(arr, target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)

if __name__ == "__main__":
    arr = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    print(binarySearch(arr, target))
    
if __name__ == "__main__":
    arr = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    k = binarySearch(arr, target)
    print(k , end = " ")

# ...........................................
    
# recursion methoud 

def binarySearch(nums , low, high, target):
    if low > high:
        return -1  # Base case
    
    # Perform the steps:
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid]  > target :
        return binarySearch(nums, mid + 1, high, target)
    return binarySearch(nums, low, mid - 1, target)

def search(nums, target):
    return binarySearch(nums, 0, len(nums) - 1, target)

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    ind = search(a, target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind) 


# also represenrt as 

def f(nums , low, high, target):
    if low > high:
        return -1  # Base case
    
    # Perform the steps:
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif  nums[mid]  > target :
        return f(nums, low, mid - 1, target)
    return f(nums, mid + 1, high, target)


if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    n = len(a)

    ind = f(a, 0, n-1, target )
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind) 





