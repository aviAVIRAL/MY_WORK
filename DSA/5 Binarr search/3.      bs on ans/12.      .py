




def pos(arr,wt , d ):
    
    s = 0 
    for i in range(len(arr)):
        s += arr[i]
        if s > wt:
            d -= 1

    if d <= 0:
        return True 
    else : 
        return False 


def f(arr, d):
    for i in range(1, 100):
        if (pos(arr,i,d)==True):
            return i 
    

arr=[1,2,3,4,5,6,7,8,9 ]
d = 15 
print(f(arr, d))
