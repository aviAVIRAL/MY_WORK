


# m1  use  pyhton library 
def f(s): 
    
    str = s[ : : -1]

    return str

if __name__=="__main__":
    s =  "aviral"
    print(f(s))


print( )
print( )
# m2 

def f(s): 

    arr = list(s)

    n = len(arr)
    
    i = 0
    j = n-1 

    while( i < j): 
        arr[i], arr[j] = arr[j], arr[i]
        i +=1 
        j -=1     
    
    str = ''.join(arr)
    
    return  str

if __name__=="__main__":
    s =  "aviral"
    print(f(s))