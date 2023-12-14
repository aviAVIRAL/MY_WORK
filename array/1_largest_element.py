# largest element of arr 

# 1. brute :
# sort()  build in function 
# sort kr and last element return kr de 
# tc = same as sorting :
# tc = o( n log n )  sc = o(1)


# 3. optimal   tc = o(n)  sc = o(1)
# m1 r1 
def largest_element(arr):
    largest = arr[0]
    n = len(arr)

    for i in range(0, n):
        if  arr[i] > largest  :
            largest = arr[i] 
    
    return largest

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)

ans = largest_element(arr)
print(ans)

# m1 r2            
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

# .......................................

# python build in function 

# 1. sort()    tc = 0(nlogn)  sc = o(1)
def f(arr, n):
    arr.sort()
    return arr[n-1]

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9999, 2, 6, 5]
    print(f(arr, len(arr)))

# 2. sorted()    tc = 0(nlogn)  sc = o(n)
def f(arr, n):
    ans = sorted(arr)
    return ans[n-1]

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9999, 2, 6, 5]
    print(f(arr, len(arr)))

# 3. max ()  tc = o(n)  sc = o(1)
def f(arr):
    ans = max(arr)
    return ans

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9999, 2, 6, 5]
    print(f(arr))

