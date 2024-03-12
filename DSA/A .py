


def search(arr, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        # if mid points the target
        if arr[mid] == k:
            return mid

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= k and k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [ 7, 15, 10, 100, 9, 101,   19, 1,  9,  2, 3,  4, 8, 6]
          # 0  1   2   3    4   5     6   7   8   9  10        13 
    n = len(arr)

    ans = search(arr, n, 6 )
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)


print()

