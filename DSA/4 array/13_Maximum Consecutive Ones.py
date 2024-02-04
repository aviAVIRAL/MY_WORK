# optimum  tc = o(n)   sc =  o(1)

def findMaxConsecutiveOnes( arr):
    count = 0
    maxi  = 0 

    for i in range ( len(arr)):
        if arr[i] == 1:
            count +=1
            # maxi  = max(count,maxi )
        else:
            count = 0
            
        maxi  = max(count,maxi )
    return maxi 

arr = [ 1,1,0,1,1,1,0,1,1]
ans = findMaxConsecutiveOnes(arr)
print(ans)