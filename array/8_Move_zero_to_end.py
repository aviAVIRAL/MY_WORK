# 1. brute forces Approch   tc =  o(n) + o(n) + o(n) = O(3n) ~> O(n)  & sc = o(n)

def Move_all_Zero_at_last(arr,n):
    temp = []

    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])

    for i in range(n):
        if arr[i] == 0:
            temp.append(arr[i])

    j =0 
    for i in range(0,n):
        arr[i] = temp[j]
        j+=1

    return arr

arr = [1,2,0,4,0,5,0,1]
ans = Move_all_Zero_at_last(arr,8) # output [1, 2, 4, 5, 0, 0, 0]
print(ans)

# print("striver brute forces ") 

# tc = 0(2n)  sc = 0(n)

def f(arr):
    n = len ( arr)
    temp =  []

    for i in range( 0 , n ):
        if arr[i] != 0 :
            temp.append(arr[i])
    
    k = len(temp)        # imp
    for i in range(0 , k):
        arr[i] = temp[i]

    for i in range( k , n):     # imp
        arr[i] = 0 

    return arr

if __name__=="__main__":
    arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    print(f(arr))    #   output [ 1, 2, 3, 2, 4, 5, 1, 0, 0, 0]

if __name__=="__main__":
    arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    Sol = f(arr)
    for x in Sol:    # for each_element in arr:
        print(x , end=" ") 
    print()                   #output  1 2 3 2 4 5 1 0 0 0



# 2. optimal solution tc = o(x) + o(n -x) ~> o(n)    sc = o(1)

# r 1  for loop  

def Move_Zero_at_last(arr,n):

    j = -1    #  - float ("inf")
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    for i in range( j+1 , n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    
    return arr


arr = [1,2,0,4,0,0,5,0]
ans = Move_Zero_at_last(arr,7) # output [1, 2, 4, 5, 0, 0, 0]
print(ans)

# r2 while loop 

def f(arr, n):
    j = -1
    i = 0

    while i < n:
        if arr[i] == 0:
            j = i
            break
        i += 1

    i = j + 1
    while i < n:
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        else:             #  imp* : else 
            i += 1

    return arr

if __name__=="__main__":
     arr = [1,2,0,4,0,0,5,0]
     n  = len(arr)
     ans = f(arr, n)
     print(ans)




# .................................................
# .................................................
    # bhai aapne aap kiya hai ye wala
     

def f(arr):
    n = len(arr)
    
    j = 0
    for i in range(n):
        if arr[i] != 0 :
            arr[j] = arr[i]
            j+=1 
      
    for i in range(j, n):
        arr[i] = 0 

    return arr 

if __name__=="__main__":
    arr = [3,2,0 , 5,0,1,0,3,2,0,4]
    print(f(arr))

        

