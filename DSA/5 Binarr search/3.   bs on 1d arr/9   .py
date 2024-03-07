




import bisect

def f(arr, target):
    n = len(arr)
    ind = bisect.bisect_left(arr, target)
    arr.insert(ind, target)
    return ind



arr = [1,3,5,6]
target = 7

print(f(arr, target))
# Output: 4      
print(arr)           
    

import bisect

def f(arr, target):
    n = len(arr)
    ind = bisect.bisect_left(arr, target)
    return ind

arr = [1,3,5,6]
target = 100

print(f(arr, target))
# Output: 4      
           


    