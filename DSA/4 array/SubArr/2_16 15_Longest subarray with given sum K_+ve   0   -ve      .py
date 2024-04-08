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


# brute : work fine using 3 loop 


def getLongestSubarray(a, k) :
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        for j in range(i, n): # ending index
            # add all the elements of
            # subarray = a[i...j]:
            s = 0
            for K in range(i, j+1):
                s += a[K]

            if s == k:
                length = max(length, j - i + 1)
    return length

if __name__ == "__main__":
    a = [-1, 1, 1]
    k = 1
    length = getLongestSubarray(a, k)
    print(f"The length of the longest subarray is: {length}")


# brute ka better version  using 2 loop

def ff(a, k) :
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        s = 0
        for j in range(i, n): # ending index
            # add the current element to
            # the subarray a[i...j-1]:
            s += a[j]

            if s == k:
                length = max(length, j - i + 1)
    return length

if __name__ == "__main__":
    a = [-1, 1, 1]
    k = 1
    length = ff(a, k)
    print(f"The length of the longest subarray is: {length}")

# ..............................

# optimal : Kadan algo its working i n all ( +ve, -ve , 0 )
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
# if __name__=="__main__":
#     arr= [ -1, 1, 1]
#     k = 1 
#     print(f(arr, k))       not working 














