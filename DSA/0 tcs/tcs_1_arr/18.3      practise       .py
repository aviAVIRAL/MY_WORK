
def f(arr):
    n = len(arr)
    mp ={ }

    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] +=1 
        else:
            mp[arr[i]] = 1
    
    return mp 

if __name__=="__main__": 
    arr = [  12,12,13,13,14,15,15]
    print(f(arr))


# from collections import OrderedDict

# # Create an ordered dictionary
# ordered_map = OrderedDict()
print("............")

from collections import OrderedDict
def f(arr):
    n = len(arr)
    mp = OrderedDict()

    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] +=1 
        else:
            mp[arr[i]] = 1
    return mp 

if __name__=="__main__": 
    arr = [  12,12,13,13,14,15,15]
    print(f(arr))

# ..........................
print()



def f(arr):
    n = len(arr)
    mp ={ }
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] +=1 
        else:
            mp[arr[i]] = 1
    return mp 
if __name__=="__main__": 
    arr = [  12,12,13,13,14,15,15]
    k = f(arr)
    for x in k :
        if k[x] == 2 :
            print(x, end = " ")
    print()

# from collections import OrderedDict

# # Create an ordered dictionary
# ordered_map = OrderedDict()
print("............")

from collections import OrderedDict
def f(arr):
    n = len(arr)
#    ordered_map = OrderedDict()
    mp = OrderedDict()


    # mp ={ }

    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] +=1 
        else:
            mp[arr[i]] = 1
    
    return mp 

# if __name__=="__main__": 
#     arr = [  12,12,13,13,14,15,15]
#     print(f(arr))

if __name__=="__main__": 
    arr = [  12,12,13,13,14,15,15]
    k = f(arr)
    for x in k :
        if k[x] == 2 :
            print(x, end = " ")
    print()

