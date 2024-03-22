
def rev(arr, start, stop):
    
    for i in range(stop//2):
        arr[i], arr[stop-1-i] = arr[stop-1-i], arr[i]
     

def f(arr):

    for i in range(len(arr)):
        if arr[i] == 1:
            rev(arr,0, i)
   
    arr.remove(1) 
    arr.remove(1) 
    return arr       
  
arr= [ 5,6,7,8,1,9,1,10]
print(f(arr ))
        









