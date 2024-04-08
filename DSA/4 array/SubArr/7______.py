

def f(arr, k):
    maxilen = -float("inf")
    sum = 0 
    ansStart = -1
    ansEnd = -1 

    for i in range(len(arr)): 
        if sum == 0 :
            start = i
        sum += arr[i]
        if sum == k:
            sum = 0 
            ansStart = start
            ansEnd = i
            maxilen = max(maxilen, ansEnd - ansStart + 1)
      
        # if sum < 0 :         #for all +ve, -ve, 0 elm 
        #     sum = 0  
    
    return maxilen  
         
if __name__=="__main__":
    arr= [ 2, 3, 5 ,1 ,9 ]
    k = 10 
    print(f(arr, k))
   
if __name__=="__main__":
    arr= [ -1, 1, 1 ]
    k = 1 
    print(f(arr, k))  # not working ecept op is 3 
                        #  but coming 1 

