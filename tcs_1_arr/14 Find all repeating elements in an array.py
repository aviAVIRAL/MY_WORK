# find all repeating element in us sorted  arr 

#  Input: arr = [1,1,2,3,4,4,5,2]
#  Output:       1,2,4


# mapping methoud 

#  dictionary = dic = mapping = mp  

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



# sorting methoud  r 1    sc = 0( n )


def f(arr):
    n = len(arr)
    arr.sort() 

    temp = [ ]
    for i in range(n-1):
        if arr[i] == arr[i+1] :
            temp.append(arr[i])
        else:
            i+= 1

    return temp 

if __name__=="__main__": 
    arr = [1,1,2,3,4,4,5,2]
    print(f(arr))


# sorting methoud  r 2     sc = 0(1 )

def f(arr):
    n = len(arr)
    arr.sort() 
    
    j = 0 
    for i in range(n-1):
        if arr[i] == arr[i+1] :
            arr[j] = arr[i]
            j +=1 
        else:
            i+= 1

    return j 

if __name__=="__main__": 
    arr = [1,1,2,3,4,4,5,2]
    k = f(arr)

    for i in range(k ):
        print( arr[i], end= " ")
    print 
    
    # for x in k :   do not use this loop, reason indexing ko access kr na hai na ki ' eachelement = x '
    #     print( x , end = " ")
    # print( ) 


