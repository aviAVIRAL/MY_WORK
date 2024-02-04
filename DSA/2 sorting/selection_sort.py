# representation - 1

def selection(arr):
    n = len(arr)  
    for i in range(n-1):
        min = i
        for j in range(i, n):
            if arr[j] < arr[min]:
                min = j
           
        arr[i], arr[min] = arr[min], arr[i] 

arr = [ 4, 65, 6, 33,2,3,1]
selection(arr)
print(arr)


# representation - 2

def selection(arr, n):
    
    for i in range(n-1):
        
        min = i
        for j in range(i, n):
            if arr[j] < arr[min]:
                min = j
           
        arr[i],arr[min] = arr[min],arr[i] 

arr = [ 4, 65, 6, 33 ,2, 3,1]
n = len(arr)

selection(arr,n)
print(arr)


