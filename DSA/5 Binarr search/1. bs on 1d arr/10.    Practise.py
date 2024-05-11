
def lowerBound(arr ,x ) -> int:
    n = len(arr)
    low = 0    # low, high = 0, n - 1
    high = n - 1   

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:  
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return low

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    x = 9
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
# op  lower bound is the index: 3
if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    x = 1111119
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
if __name__ == "__main__":
    arr = [3, 5, 8, 9 , 15, 19]
    x = 9
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)
# op  lower bound is the index: 3


# cp  

# build in liberary/module => bisect | same tc sc as binary search  
# tc log n : sc 1 

import bisect

def lowerBound(arr, x):

    return bisect.bisect_left(arr, x)

if __name__ == "__main__":
    arr = [3, 5, 8, 15,15,15, 19]
    x = 9  # op The lower bound is the index: 3
    ind = lowerBound(arr, x)
    print("The lower bound is the index:", ind)


# ..................representation..............
# import bisect
# import bisect as bs
# from bisect import bisect_left
    
# ...................................................
    # concept to inser the elm in arr 