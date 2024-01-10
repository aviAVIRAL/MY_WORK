#  dictionary = dic = mapping = mp  

# Find all the non-repeating elements in an array


# mapping  
def f(arr):
    n = len(arr)
    mp ={ }

    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] +=1 
        else:
            mp[arr[i]] = 1
    
    temp = [ ]
    for x in mp: 
        if mp[x]  == 1 :
            temp.append(x) 

    return temp 

if __name__=="__main__": 
    arr = [   9  ,1,1,2,2,2,  3   ,4,4,  5  ,6,6,  7]
# output : [9, 3, 5, 7]
    print(f(arr))




# sorting se   sc = 0( n )

def f(arr):
    n = len(arr)
    arr.sort() 

    temp = []

    if arr[0] != arr[1] :
        temp.append(arr[0])


    for i in range(1, n-1):
        if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
            temp.append(arr[i])
        else:
            i+=1

    if arr[n-1] != arr[n-2]:
        temp.append(arr[n-1])

    return temp 

if __name__=="__main__": 
    arr = [  9   ,1,1,2,2,2,  3   ,4,4,  5  ,6,6,  7]

# imp  sorted arr = [ 1,1,2,2,3,4,,4,,5,6,6,7,9]  
# output [3, 5, 7, 9]
    print(f(arr))


