

def f(arr , k ): 
    n = len(arr)
    
    length = 0
    cnt = 0    # see her 
    for i in range(n):
        for j in range(i, n):
            s = 0
            for K in range(i, j + 1):
                s += arr[K]

            if s == k:    
                cnt += 1   # see her 
                length = max ( length ,  j+1  -i )

    return length, cnt 

if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    print(f(arr , k ))

# (3, 2) op
# (3, 3) op 
if __name__ == "__main__":
    arr = [1, -1, 1]
    k = 1
    print(f(arr , k ))
