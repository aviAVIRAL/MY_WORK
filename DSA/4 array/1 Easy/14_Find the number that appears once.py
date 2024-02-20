# jo number only ek bar auye usko print kr de 

# ip arr = [ 1,1,  2,  3,3,  4,4]
# op 2 
# .............

# 1. brute approach  #  tc = o(n^2)

#  code will run but error :- TLE   time limitation exceeded   error showing when submite

# r1
def f(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i] :
                count += 1
        if count == 1:
            return arr[i]

if __name__=="__main__":
    arr = [ 1,1,  2,  3,3,  4,4]
    ans = f(arr)
    print(ans)

# r2
def get_Single_Element(arr):
    for i in range(len(arr)):
        num = arr [i]
        count = 0
        for j in range(len(arr)):
            if arr[j] == num :
                count += 1
        if count == 1:
            return num

arr = [ 1,1,  2,  3,3,  4,4]
ans = get_Single_Element(arr)
print(ans)


# 2. better 

# code will run but not able to pass the hidden test case in leed code 
# hasing use 


def onces(arr): 
    n = len(arr)
    hash = [0]*(100)

    for i in range(n): 
        hash[arr[i]] +=1 
    
    for j in range(len(hash)):
        if hash[j] == 1 :
            break
    
    return j 

if __name__=="__main__":
    arr = [ 1,1,  2,  3,3,  4,4]
    ans = onces(arr)
    print(ans)
 
# 3 optimal   tc = 0(n)  sc = 0(1)

# r1

def f(arr):
    xor = 0 
    for x in arr :
        xor = xor ^ x 
    return xor 

if __name__=="__main__": 
    arr = [1, 1, 2, 3, 3, 4, 4]
    print(f(arr))

# r2 
def getSingleElement(arr):
    xorr = 0
    for i in range(len(arr)):    # for each_elelmnet in arr:
        xorr = xorr ^ arr[i]     # xorr = xorr ^ each_element
    return xorr

arr = [1, 1, 2, 3, 3, 4, 4]
ans = getSingleElement(arr)
print("The single element is:", ans)




# .//....................can be ignore ........
# leed Code  one line ans 


def occures_only_ones( nums) :
    return sum(list(set(nums)) * 2) - sum(nums)


arr = [  1,1,     2,    3,3,  4,4  ]
ans = occures_only_ones(arr)
print(ans)
