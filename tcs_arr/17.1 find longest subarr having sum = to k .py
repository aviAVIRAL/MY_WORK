# Longest Subarray with given Sum K(Positives

# input  k =  10   arr = [ 2 , 3 , 5 , 1 ,9 ]
# [2 + 3 + 5] =  10 
# [1 + 9] = 10 
# but   [2 + 3 + 5] longest hai  length is 3 
# output : 3 

# brute 

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



# better  : 
    
    
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

