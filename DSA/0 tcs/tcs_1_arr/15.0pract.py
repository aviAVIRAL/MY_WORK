

print()

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
   
    temp = []
    for i in range(len(arr)):
        temp.append(mp[arr[i]])

    return temp

if __name__=="__main__": 
    arr =  [20, 15, 26, 2, 98, 6]

    sol = f (arr)

    for x in sol: 
        print(x, end=" ")
