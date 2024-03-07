

# .......... using bisect 
import bisect

def f(arr, x):
    lb = bisect.bisect_left(arr, x )
    ub = bisect.bisect_right(arr, x ) - 1  # imp

    if lb == len(arr):
        lb = -1
    if ub == len(arr): 
        ub = -1    

    return lb, ub 

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    k = 8
    ans = f(arr,k)
    print("The first and last positions are:", ans[0], ans[1])


# .......... using bisect 
import bisect

def f(arr, x):
    lb = bisect.bisect_left(arr, x )
    ub = bisect.bisect_right(arr, x ) - 1  # imp

    if lb == len(arr):
        lb = -1
    if ub == len(arr)-1: 
        ub = -1    

    return lb, ub 

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    k = 3338
    ans = f(arr,k)
    print("The first and last positions are:", ans[0], ans[1])


