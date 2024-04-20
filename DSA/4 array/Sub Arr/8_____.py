
def f(arr , k ): 
    n = len(arr)
    
    length = 0
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            s = 0
            for K in range(i, j + 1):
                s += arr[K]

            if s == k:
                cnt += 1 
                length = max ( length ,  j+1  -i )

    return length, cnt 

if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    print(f(arr , k ))
if __name__ == "__main__":
    arr = [1, -1, 1]
    k = 1
    print(f(arr , k ))

print()
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
