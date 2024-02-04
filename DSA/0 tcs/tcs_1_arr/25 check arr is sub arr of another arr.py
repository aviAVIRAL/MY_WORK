# Check if array is subset of another array.

# Examples:

# Example 1:
# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [2,4,3,1,7,5,15]
# Output: arr1[] is a subset of arr2[]

# Example 2:
# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [4,5,2]
# Output: arr1[] is not a subset of arr2[]

# Example 3:
# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [11,12,13,15,16]
# Output: arr1[] is not a subset of arr2[]


def f(arr1 , arr2):

    n = len(arr1)
    m = len(arr2)

    if n > m : 
        return False
    
    for i in range(n):
        
        if arr1[i] not in arr2 :      
            return False
    
    return True

if __name__=="__main__":
    arr1 = [1,3,4,5,2]
    arr2 = [2,4,3,1,7,5,15]

    print(f(arr1 , arr2 ))

print( )

if __name__=="__main__":
    a1 = [1,3,4,5,2]
    a2=  [11,12,13,15,16]

    print(f(a1 , a2 ))


print ()

if __name__=="__main__":
    a1 = [1,3,4,5,2 ,22,33,4,4,55,88,88,]
    a2=  [11,12,13,15,16]

    print(f(a1 , a2 ))
    