



def f(arr, k):
    maxilen = -float("inf")
    sum = 0 
    ansStart, ansEnd = -1 , -1 

    for i in range(len(arr)): 
        if sum == 0 :
            start = i
        sum += arr[i]
        if sum == k:
            sum = 0 
            ansStart = start
            ansEnd = i
            maxilen = max(maxilen, ansEnd - ansStart + 1)
        # if sum < 0 : for all +ve, -ve, 0 elm 
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


print()
print()




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


print()



def longest_subarray_with_sum_k(arr, k):
    max_length = 0
    prefix_sum = 0
    prefix_sum_map = {0: -1}  # Initialize with prefix sum 0 at index -1

    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_sum - k in prefix_sum_map:
            start_index = prefix_sum_map[prefix_sum - k]
            subarray_length = i - start_index
            max_length = max(max_length, subarray_length)

        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = i

    return max_length

# Example usage:
arr = [-1, 1, 1]
k = 1
print(longest_subarray_with_sum_k(arr, k))  # Output: 3

print()
def longest_subarray_with_sum_k(arr, k):
    maxi = 0
    pre = 0
    mp = {0: -1}  # Initialize with prefix sum 0 at index -1

    for i in range(len(arr)):
        pre += arr[i]
        
        if pre - k in mp:
            satrt = mp[pre - k]
            leng = i - satrt
            maxi = max(maxi, leng)

        if pre not in mp:
            mp[pre] = i

    return maxi

# Example usage:
arr = [-1, 1, 1]
k = 1
print(longest_subarray_with_sum_k(arr, k))  # Output: 3










