
# kadan se ho geya   

# 0 + ve 

# tc n   sc 1 
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
    
    return maxilen  
         
if __name__=="__main__":
    arr= [ 2,3,5 ]
    k =  5
    print(f(arr, k))
if __name__=="__main__":
    arr= [ 2, 3, 5 ,1 ,9 ]
    k = 10 
    print(f(arr, k))

# Example 1:
# Input Format: N = 3, k = 5, array[] = {2,3,5}
# Result:          2
# Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

# Example 2:
# Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
# Result:          3
# Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.
