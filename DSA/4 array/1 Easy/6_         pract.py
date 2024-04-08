



# Q 1 return "Count" / total number of, unique element 
def f(arr) : 
    s = set()

    n = len(arr)

    for i in range(n):
        s.add(arr[i])
    
    k = len(s)
    j = 0
    for x in s:
        arr[j] = x
        j += 1

    return k  # or return j 

# output will : 3  only 
if __name__ == "__main__":
    arr = [1, 1, 2,  2, 2, 3, 3]
    print(f(arr))

print()

# .....................................

# Q 1 return "Count" / total number of, unique element 
def f(arr) : 
    s = set()

    n = len(arr)

    for i in range(n):
        s.add(arr[i])
    
    return s 
# output will : 3  only 
if __name__ == "__main__":
    arr = [1, 1, 2,  2, 2, 3, 3]
    print(f(arr))

print("...")

# Q 1 return "Count" / total number of, unique element 
def f(arr) : 
    s = set()

    n = len(arr)

    s.update(arr)
    
    return s 
# output will : 3  only 
if __name__ == "__main__":
    arr = [1, 1, 2,  2, 2, 3, 3,4,5]
    print(f(arr))

print("?????")


def f(arr) : 
    s = set(arr)

    return s 
if __name__ == "__main__":
    arr = [1, 1, 2,  2, 2, 3, 3,4,5,6,7,8]
    print(f(arr))


print("?????")


def f(arr) : 
    s = set(arr)
    
    temp = []
    for x in s : 
        temp.append(x)

    return temp 
# output will : 3  only 
if __name__ == "__main__":
    arr = [1, 1, 2,  2, 2, 3, 3,4,5,6,7,8]
    print(f(arr))











