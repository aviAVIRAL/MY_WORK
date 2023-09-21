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


# 2 . better  tc = o(2n)  sc = o(n)
# use kiya hashing  concept

def find_missing_number(arr):
    n = len(arr)
    Hash = [0] * (n + 20)

    for i in range(n):
        Hash[arr[i]] += 1

    for i in range(1, n + 20):
        if Hash[i] == 0:
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