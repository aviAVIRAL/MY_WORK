# LINEAR SEARCH 
# tc = o(n)   sc = o(1)

def linear_search(arr,n,nums):
    for i in range (n):
        if arr[i] == nums:
           return i
    
    else:  # imp ~ * pura loop iterate ke baad else mein jana hai  
        return -1
        
      
arr = [ 1,2,3,4,5,6] 

ans = linear_search(arr, 6 , 4)
print(ans)

print()
      
arr = [ 1,2,3,4,5,6] 

ans = linear_search(arr, 6 , 10)
print(ans)

