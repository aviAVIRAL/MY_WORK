# Two Sum : Check if a pair with given sum exists in Array
# Problem Statement: Given an array of integers arr[] and an integer target.

# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

# Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.

# Examples:

# Example 1:
# Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
# Result: YES (for 1st variant)
#        [1, 3] (for 2nd variant)
# Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

# Example 2:
# Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
# Result: NO (for 1st variant)
# 	[-1, -1] (for 2nd variant)
# Explanation: There exist no such two numbers whose sum is equal to the target.





# concept 

# code to correct hai but according to quetion chalna hai bhaio 
def f (arr, k):

    for x in arr:          # k = 14  arr=[2,7,40 ]  ya ha 7 two time add ho raha hai ,but according to  quetion 2 elements hai jiska sum == k :
        for y in arr: 
            if x + y == k :
                return True
    return False 

if __name__=="__main__":
    arr = [2,7,2]
    k = 14 
    print(f(arr, k))


# Brute  1   tc = 0(n^2)    sc =  0(1)  

def f (arr, k):
    n = len(arr)

    for i in range(n):
        for j in range(n): 
            if i == j :
                continue
            if arr[i] +arr[j] == k : 
                return i, j 
            
    return -1 


if __name__=="__main__":
    arr = [ 2, 6 ,5,  8  ,11 ]
    k = 14        # 6 + 8 = 14 index op is (1, 3)
    print(f(arr, k))


# brute 2    tc slightly lesser than = 0(n^2) 
    
def f (arr, k):
    n = len(arr)

    for i in range(n):
        for j in range( i+1 , n): 
            if arr[i] +arr[j] == k : 
                return i, j 
            
    return -1 


if __name__=="__main__":
    arr = [ 2, 6 ,5,  8  ,11 ]
    k = 14        # 6 + 8 = 14 index op is (1, 3)
    print(f(arr, k))
        

# better  tc = 0(n)  sc =0(n)

# r1 
def two_sum(arr, k):
    n = len(arr)
    mp = {}

    for i in range(n):
        ans = k - arr[i]
        
        if ans in mp:
            return mp[ans], i
        else:
            mp[arr[i]] = i

    return -1

if __name__ == "__main__":
    arr = [2, 6, 5, 8, 11]
    k = 14
    print(two_sum(arr, k))


# r2
print( )

def f (arr, k):
    n = len(arr)
    mp = {}

    for i in range(n):
        ans = abs(k - arr[i])

        if ans not in mp: 
            mp[arr[i]] = i 
        elif ans in mp : 
            return i , mp[ans] # mp[arr[i]] nhi , mp[ans] hai caerfull  
 # other wise error ki arr[i] abhi tak mp mein hai hee nhi or tum return kr ra hai ho 

    return -1 


if __name__=="__main__":
    arr = [ 2, 6 ,5,  8  ,11 ]
    k = 14        # 6 + 8 = 14 index op is (1, 3)
    print(f(arr, k))




# optimal   tc = 0(n)+0(nlogn) sc = 0(1)

def two_sum(n, arr, target):
    
    arr.sort()

   # left, right = 0, n - 1
    left = 0
    right = n - 1
    
    while left < right:
        
        total = arr[left] + arr[right]
        
        if total == target:
            return "YES"
        
        elif total < target:
            left += 1
        
        else:
            right -= 1
    
    return "NO"

if __name__ == "__main__":
    n = 5
    arr = [2, 6, 5, 8, 11]
    target = 14
    ans = two_sum(n, arr, target)
    print("This is the answer for variant 1:", ans)




