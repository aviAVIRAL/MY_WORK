# def f(arr):
#     n = len(arr)
#     larg = arr[0]
#     i = 0 
#     while i < n:
#         # larg = arr[0]
#         if arr[i]>larg:
#             larg =  arr[i] 
#         i+=1
#     return larg

# if __name__=="__main__":
#     arr = [ 1,2,6,88,42,5,7,99,100]
#     print(f(arr))


def f(arr):
    n = len(arr)
    largest = arr[0]
    i = 0 
    while i < n:           # or   i <= n-1 :
        if arr[i]>largest:
            largest =  arr[i] 
        i+=1
    return largest

if __name__=="__main__":
    arr = [ 1,2,6,100,42,5,7,99,1000]
    print(f(arr))

def f(arr):
    n = len(arr)
    largest = arr[0]
    i = 0

    while i < n:  # Alternatively, you can use "while i <= n - 1:"
        if arr[i] > largest:
            largest = arr[i]
        i += 1

    return largest

if __name__ == "__main__":
    arr = [1, 2, 6, 100, 42, 5, 7, 99, 1000]
    print(f(arr))

               