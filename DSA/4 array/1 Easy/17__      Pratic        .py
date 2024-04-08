

# ......................
# r1
    

def f(a, k):
    n = len(a)
                    # left, right = 0, 0
    
    i = 0
    j = 0

    Sum = a[0]
    maxLen = 0
    
    while i < n:
        while j <= i and Sum > k:
            Sum -= a[j]
            j += 1
        
        if Sum == k:
            maxLen = max(maxLen, i - j + 1)
        
        i += 1
        if i < n:
            Sum += a[i]
    
    return maxLen

if __name__ == "__main__":
    a = [2, 3, 5, 1, 9]
    k = 10
    length = f(a, k)
    print(f"length of longest subarray is: {length}")




# r1

def f(a, k):
    n = len(a)
                    # left, right = 0, 0
    i = 0
    j = 0

    Sum = a[0]
    maxLen = 0
    
    while i < n:
        while j <= i and Sum > k:
            Sum -= a[j]
            j += 1
        
        if Sum == k: maxLen = max(maxLen, i - j + 1)
        
        if i < n: Sum += a[i]
        i += 1   # see here updation .................
    
    return maxLen

if __name__ == "__main__":
    a = [2, 3, 5, 1, 9]
    k = 10
    length = f(a, k)
    print(f"length of longest subarray is: {length}")

# trick 
# while j <= i and Sum > k: Sum -= a[j]; j += 1






# r1
    

def f(a, k):
    n = len(a)
                    # left, right = 0, 0
    
    i = 0
    j = 0

    Sum = a[0]
    maxLen = 0
    
    while i < n:
        while j <= i and Sum > k:  Sum -= a[j] ; j += 1
        if Sum == k: maxLen = max(maxLen, i - j + 1)
        i += 1
        if i < n: Sum += a[i]
    
    return maxLen

if __name__ == "__main__":
    a = [2, 3, 5, 1, 9]
    k = 10
    length = f(a, k)
    print(f"length of longest subarray is: {length}")








