# first increase than decrese 

def f(arr):
    n = len(arr)
    arr.sort()
   
    arr[:] = arr[ : n//2] +  arr[n//2 : n ][ : : -1]  # imp

    return arr

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    
    print(f(arr))

# output  [   1, 2, 3, 4,   9, 8, 7, 6, 5   ]

# m2
arr = [8, 7, 1, 6, 5, 9]
n = len(arr)
arr.sort()

for i in range(n // 2):
    print(arr[i], end=" ")

for i in range(n - 1, n // 2 - 1, -1):
    print(arr[i], end=" ")
