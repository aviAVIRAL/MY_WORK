
import math

def fun(arr, hourly):    
    n = len(arr)
    totalH = 0

    for i in range(n):
        totalH += math.ceil(arr[i] / hourly)
    return totalH

def f(arr, h):
    low = 1
    high = max(arr)  # 11

    while low <= high:
        mid = (low + high) // 2
        totalH = fun(arr, mid) # imp 
        if totalH <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

if __name__=="__main__":
    arr = [3,6,7,11]
    h = 8
    ans = f(arr, h)
    print("Koko should eat at least", ans, "bananas/hr.")



import math

def possible(arr, hourly, h):    
    n = len(arr)
    totHr = 0

    for i in range(n):
        totHr += math.ceil(arr[i] / hourly)
    
    if totHr <= h:
        return True
    else:
        return False

def f(arr, h):
    low = 1
    high = max(arr)  # 11

    while low <= high:
        mid = (low + high) // 2
        if possible(arr, mid, h):
            high = mid - 1
        else:
            low = mid + 1
    return low

if __name__=="__main__":
    arr = [3,6,7,11]
    h = 8
    ans = f(arr, h)
    print("Koko should eat at least", ans, "bananas/hr.")
