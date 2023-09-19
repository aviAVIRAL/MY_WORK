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