# find all repeating element in us sorted  arr 

#  Input: arr = [1,1,2,3,4,4,5,2]
#  Output:       1,2,4


# hashMap  methoud 

#  dictionary = dic = mapping = mp{ }  = HashMap    

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
        if mp[x]  != 1 :
            temp.append(x) 

    return temp 

if __name__=="__main__": 
    arr = [1,1,2,3,4,4,5,2]
    print(f(arr))




# optmial { i did it with my own }

# tc = nlogn + n 
#    sorting + linear

# sc = n : i can optimize sc also by using concept also   

print()
print()

def fu(arr):
    arr.sort()
    temp = []
    n = len(arr)
# edge case
    if arr[0] == arr[1]:
        temp.append(arr[0]) 

    for i in range(1, n- 1):
        if arr[i] == arr[i-1] or arr[i] == arr[i+1]:
            if arr[i] != temp[-1]:
                temp.append(arr[i])

# edge case
    if arr[n-2] == arr[n-1]:
        if arr[n-1] != temp[-1]:
            temp.append(arr[n-1]) 

    return temp

if __name__=="__main__": 
    arr = [1,1,1,1,2,3,3,3,3,4,5,5,5,6,6]
    print(fu(arr))

