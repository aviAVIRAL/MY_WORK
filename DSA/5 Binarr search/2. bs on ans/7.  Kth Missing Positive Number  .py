# Kth Missing Positive Number
# Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer ‘k’. Find the ‘kth’ positive integer missing from ‘vec’.

# Examples
# Example 1:
# Input Format: vec[]={4,7,9,10}, k = 1
# Result: 1
# Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.
# Example 2:
# Input Format: vec[]={4,7,9,10}, k = 4
# Result: 5
# Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 4, the fourth missing element is 5.


# ..........           ........
# aapne aap kiya by frequency hashing 

def f(a, k):
    fre = [0]*13
    for i in range(len(a)):
        fre[a[i]]  += 1
    fre.pop(0)
    
    print(fre) #[0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]    

    cnt = 0 
    for j in range(1, len(fre)):
        if fre[j] == 0 : cnt += 1 
        if cnt == k: break
   
    return j
arr= [ 2,3,4,7,11]
print(f(arr, 5))

# op 
# 9

# .............        ...................

# brut tc n    

def missingK(vec, n, k):
    for i in range(n):
        if vec[i] <= k:
            k += 1  # shifting k
        else:
            break
    return k

vec = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)

# optimal  tc log n 

def missingK(vec, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1

vec = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)







