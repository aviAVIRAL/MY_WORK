# secound largest element in an arr 

# 1. brute forces approach 
# tc = 0( n log n ) + o( n )

def sec_largest(arr):
    n = len(arr)
    first_largest = arr[n-1]

    for i in range(n-2, -1 , -1):
        if arr[i] != first_largest:
            secound_largest = arr[i]
            break 
    return(secound_largest)


arr =  [3,7,8,4,1, 92, 10]
print("orginal arr:", arr)

sorted_array = sorted(arr)
print("sorted arr:" , sorted_array)

Answer = sec_largest(sorted_array)
print("sec largest elemtment :", Answer)


# 2. better approach
# tc =  o(2n)


def sec_largest(arr):
    largest = arr[0]
    n = len(arr)
    for i in range(0, n):
        if arr[i] > largest:
            largest = arr[i]

    sec_largest =  - 1 
    for i in range(0, n):
        if arr[i] > sec_largest and arr[i] != largest :
            sec_largest = arr[i]

    return sec_largest 

arr = [6, 7, 3, 4, 65, 21]
ans = sec_largest(arr)
print(ans)

# 3. optimal approach
# tc =  o(n)

def sec_largest_element(arr):
    largest = arr[0]
    sec_largest = -float('inf')
    n = len(arr)
    for i in range(1, n):
        if arr[i] > largest:
            sec_largest = largest
            largest = arr[i]

        elif arr[i] < largest and arr[i] > sec_largest :
            sec_largest = arr[i] 
    
    return sec_largest

arr = [12,3,45,67,4,58,83]
print("original arr:" , arr)
ans = sec_largest_element(arr)
print(ans)


# quetion: Secound smallest element in arr

# + float (infinity)
# symboll chnages 


def sec_smallest_element(arr):
    smallest = arr[0]
    sec_smallest = float('inf')
    n = len(arr)
    for i in range(1, n):
        if arr[i] < smallest:
            sec_smallest = smallest
            smallest = arr[i]
        elif arr[i] > smallest and arr[i] < sec_smallest:
            sec_smallest = arr[i]
    
    return sec_smallest

arr = [12,  3  ,45,67,   4   ,58,83]
print("Original array:", arr)
ans = sec_smallest_element(arr)
print("Second-smallest element:", ans)








