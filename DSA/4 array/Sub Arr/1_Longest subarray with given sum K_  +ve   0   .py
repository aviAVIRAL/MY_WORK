# Longest Subarray with given Sum K(Positives

# input  k =  10   arr = [ 2 , 3 , 5 , 1 ,9 ]
# [2 + 3 + 5] =  10 
# [1 + 9] = 10 
# but   [2 + 3 + 5] longest hai  length is 3 
# output : 3 

# ...................................

# brute  - 1     tc n^3  sc 1 

def f(arr , k ): 
    n = len(arr)
    
    length = 0

    for i in range(n):
        for j in range(i, n):
            s = 0
            for K in range(i, j + 1):
                s += arr[K]

            if s == k:
                length = max ( length ,  j+1  -i )

    return length

if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    print(f(arr , k ))


# brute - 2   :    tc n^2    sc 1 
    
def f(arr , k ): 
    n = len(arr)
    length = 0

    for i in range(n):
        s = 0 
        for j in range(i, n):
            s += arr[j]
            if s == k:
                length = max ( length ,  j+1  -i )

    return length

if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10

    print(f(arr , k ))

# ........................................
# ............. H A S  M a p ...........................

# better 1  : + , 0 , -    for all edge cases 
    
    # tc = 0(n)^2  sc = 0(n)

def f(arr, k):
    n = len(arr)  # size of the array.
    mp = {}
    sum = 0
    MaxiLen = 0
    for i in range(n):

        sum += arr[i]

        if sum == k:
            MaxiLen = max(MaxiLen, i + 1)

        rem = sum - k
        if rem in mp:
            length = i - mp[rem]
            MaxiLen = max(MaxiLen, length)

        if sum not in mp:  #edge case for zeros 
            mp[sum] = i

    return MaxiLen

if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    length = f(arr, k)
    print(f"The length of the longest subarray is: {length}")

if __name__ == "__main__":
    a = [-1, 1, 1]
    k = 1
    length = f(a, k)
    print(f"The length of the longest subarray is: {length}")

# ..........................      .................
# ..........................      .................

# optimal 2 { 2 poiner greedy }  for   +ve  and zero's    elm only 
    # tc = 0(2n)  *tc :::::  sc = 0(1)

# ye approrach kaam kr be sakti hai or nhi bee 

print()

# represent by avi 

def func(a, k):
    n = len(a)
    i = 0
    j = 0
    Sum =  0   # a0]
    maxLen = 0
    while i < n:
        Sum += a[i]

        if Sum == k:
            maxLen = max(maxLen, i - j + 1)

        while j <= i and Sum > k:
            Sum -= a[j]
            j += 1
        
        
        i += 1                      
        # if i < n:
        #     Sum += a[i]

    return maxLen
if __name__ == "__main__":
    a = [2, 3, 5, 1, 9]
    k = 10
    length = func(a, k)
    print(f"{length}")


if __name__ == "__main__":
    a = [-1, 1, 1]
    k = 1
    length = func(a, k)
    print(f"{length}")

    
# represent by striver 

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
    print(f"The length of the longest subarray is: {length}")

# ...................,,,,,,,,,,,,,,,,,....
# ,,,,,,,,,,,,,,,,,,,,,,..................
