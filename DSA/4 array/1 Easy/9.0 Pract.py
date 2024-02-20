print()
print( )
# print( ).................................


def f (arr ):
    n = len(arr)
    temp = []

    for i in range ( n):
        if  arr[i] == 0 :
            temp.append(arr[i])
    for x in arr : 
        if x == 1 : 
            temp.append(x)
    for x in arr : 
        if x == 2 : 
            temp.append(x)

    j = 0 
    for i in range(len(temp)): 
        arr[j] = temp[i]
        j += 1 

    return arr 

if __name__=="__main__":
    arr= [2,0,1,0,1,2]
    print(f(arr))

    









