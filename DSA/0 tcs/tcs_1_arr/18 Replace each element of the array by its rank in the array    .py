
# Replace elements by its rank in the array

# Problem Statement: Given an array of N integers, the task is to replace each element of the array by its rank in the array.

# Examples:

# Example 1:
# Input: 20 15 26 2 98 6
# Output: 4 3 5 1 6 2
# Explanation: When sorted,the array is 2,6,15,20,26,98. So the rank of 2 is 1,rank of 6 is 2,rank of 15 is 3 and so…

# Example 2:
# Input: 1 5 8 15 8 25 9
# Output: 1 2 3 5 3 6 4
# Explanation: When sorted,the array is 1,5,8,8,9,15,25. So the rank of 1 is 1,rank of 5 is 2,rank of 8 is 3 and so…





#  m 1  r 1 

arr = [20, 15, 26, 2, 98, 6]
n = len(arr)

mp = {}
temp = 1
brr = arr.copy()
brr.sort()

for i in range(n):
    if brr[i] not in mp:  # Check if key exists in the dictionary
        mp[brr[i]] = temp
        temp += 1

for i in range(n):
    print(mp[arr[i]], end=" ")


print( )

#  m 1   r 2


print( )

def  f ( arr ):
    n = len(arr)
    mp = {}
    temp = 1
    brr = arr.copy()
    brr.sort()

    for i in range(n):
        if brr[i] not  in mp :
            mp[brr[i]] = temp
            temp += 1

    # return mp
    

if __name__=="__main__": 
    arr =  [20, 15, 26, 2, 98, 6]

    f (arr)

    for i in range(n):
        print(mp[arr[i]], end=" ")

print( )



#  m 2  r 1 

arr = [20, 15, 26, 2, 98, 6]
n = len(arr)

mp = {}


temp = 1
brr = arr.copy()
brr.sort()

for i in range(n):
    if mp.get(brr[i], 0) == 0:
        mp[brr[i]] = temp
        temp += 1

for i in range(n):
    print(mp[arr[i]], end=" ")


print( )

#  m 2  r 2

print( )

def  f ( arr ):
    n = len(arr)
    mp = {}
    temp = 1
    brr = arr.copy()
    brr.sort()

    for i in range(n):
        if mp.get(brr[i], 0) == 0:
            mp[brr[i]] = temp
            temp += 1

    # return mp
    

if __name__=="__main__": 
    arr =  [20, 15, 26, 2, 98, 6]
                                                                                                                                                                                                                                                                                      
    f (arr)

    
    for i in range(n):
        print(mp[arr[i]], end=" ")





