# Example 1:
# Input Format:
#  N = 3, k = 5, array[] = {2,3,5}
# Result:
#  2
# Explanation:
#  The longest subarray with sum 5 is {2, 3}. And its length is 2.

# Example 2:
# Input Format
# : N = 3, k = 1, array[] = {-1, 1, 1}
# Result:
#  3
# Explanation:
#  The longest subarray with sum 1 is {-1, 1, 1}. And its length is 3.





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
        
        if sum < 0 :
            sum = 0   # impo 

    return maxilen  
         
if __name__=="__main__":
    arr= [ 2,3,5 ]
    k =  5
    print(f(arr, k))
if __name__=="__main__":
    arr= [ -1, 1, 1]
    k = 1 
    print(f(arr, k))



print()
print()


def f(arr, k):
    n = len(arr) 

    pre = 0
    suff = 0

    maxi = float('-inf')
    
    sta, end = -1, -1 

    for i in range(n):
        if pre > k : 
            start = i 

        if pre >k :
            pre = 0
            sta = start
            end = i 
        # if suff >k :
        #     suff = 0
            maxi = max(maxi, end - sta+1)
            
        pre += arr[i]    #    pre = pre * arr[i]
        # suff += arr[n - i - 1]
        

    return maxi

arr = [1, -1 , 1 ] 
k = 1
print(f(arr,k ))












