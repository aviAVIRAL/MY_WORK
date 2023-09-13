# 1. brute forces  tc = o(n)  sc =o(n)

def rotate_by_1_place(arr):
    n = len(arr)
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]  # This line should be outside the loop
    return temp

arr = [1, 2, 3, 4, 5]
print("original arr:",arr)
ans = rotate_by_1_place(arr)
print("rotaed by 1 :" ,ans)


# 2 . Optimum approach  tc = o(n)  sc = o(1)

def rotat_by_1(arr):
    n = len(arr)
    temp = arr [ 0 ]
    for i in range (1, n):
        arr[i - 1] = arr [i]

    arr[n - 1] = temp  # pure loop ke iterrate ke baad last mein...
    return arr

arr = [1, 2, 3, 4, 5]
ans = rotat_by_1(arr)
print(ans)

