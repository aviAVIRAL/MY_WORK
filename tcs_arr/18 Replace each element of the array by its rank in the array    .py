
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
        if brr[i] in mp :
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





