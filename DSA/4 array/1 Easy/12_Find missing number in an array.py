

# brute hai aapne aap kr diya  | tc = 0(n^2) | sc 0(1)


def f(a):
    n = len(a)

    for i in range(n+1): 
        for j in range(n):
            if  i ==   a[j] :
                break
        if i !=  a[j] :
            break 
    return i  
            
arr = [0,1, 3,4,5]
print(f(arr))
arr = [0,1,2, 3,4,5,6,    8]
print(f(arr))                             


# 1. brute force   tc = o(n*n) ~> n^2    sc = o(1) 

def missing_value(arr):

    for i in range( len(arr)+1):   # n = len(arr)
        flag = 0
        for j in range(len(arr)):  
            if arr[j] == i :
                flag = 1
                break
        if flag == 0 :
            break
    return i 
  

arr =[0, 1, 2, 3,     5 ,6 ]
ans = missing_value(arr )
print (ans)


# 2 . better  tc = o(n + n)  sc = o(n)

# use kiya " hashing " ~> frequenc : concept

def find_missing_number(arr):
    n = len(arr)
    freq = [0] * 100

    for i in range(n):
        freq[arr[i]] += 1

    for i in range(1, 100):
        if freq[i] == 0:
            break

    return i

arr =[1,2,3,5]
ans =find_missing_number(arr)
print(ans)
print()
arr =[1,2,1,3,5]
ans =find_missing_number(arr)
print(ans)
print()
arr =[3,0,1,2]
ans =find_missing_number(arr)
print(ans)

print("optimal sol" )

#  3. optimal   tc = o(n)  sc = o(1)

def missingNumber(arr , N): 

    summation = (N * (N + 1)) // 2   # here N is not a size of arr :-len(arr) & N is bigest number that its .it will predefine in quetionn gfg or leedcode  
  
    X = sum(arr)

    ans = summation - X
    
    return ans

N = 5
arr =[1,2,3,5]
ans =missingNumber(arr, N)
print(ans)
print()
N = 5
arr =[0,1,2,3,5]
ans =missingNumber(arr, N )
print(ans)

# concept 
N = 3 # max number in arr [ 1 , 2 , 3]
summation = (N * (N + 1)) // 2
print(summation)  
