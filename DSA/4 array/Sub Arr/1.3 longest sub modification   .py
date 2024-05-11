

# modification 

# bus print kr diya all sub array 





def f(arr, k):
    n = len(arr)  # size of the array.
    mp = {}
    sum = 0
    subarrays = []

    for i in range(n):
        sum += arr[i]
        if sum == k:
            subarrays.append(arr[   :  i + 1])
        if sum - k in mp:
            subarrays.append(arr[mp[sum - k] + 1  :  i + 1 ])
        if sum not in mp:  # edge case for zeros 
            mp[sum] = i

    return subarrays                    

if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    ans = f(arr, k)
    for x in ans:
        print(x, end = " ")
    print()                  # op [2, 3, 5] [1, 9]
    
    # k = 10
    # ans = f(arr, k)
    # for x in ans:
    #     print(x)




def f(arr, k):
    n = len(arr)  # size of the array.
    mp = {}
    sum = 0
    subarrays = []

    for i in range(n):
        sum += arr[i]
        if sum == k:
            subarrays.append(arr[   :  i + 1])
        if sum - k in mp:
            subarrays.append(arr[mp[sum - k] + 1  :  i + 1 ])
        if sum not in mp:  # edge case for zeros 
            mp[sum] = i

    return subarrays                    

if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    ans = f(arr, k)
    for x in ans:
        print(*x)  # impo 
                    
                    # op   2 3 5
                        #  1 9
    
# .............concept..............

for _ in range(int(input())):
    k = int(input())
    arr = list(map(int, input().split()))

    maxi = -1
    n = len(arr)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == k and (j - i + 1) > maxi : 
                # maxi = max(maxi, j - i + 1 )
                maxi = j - i + 1
                subarr = arr[i: j + 1]
    print(maxi, subarr)

# # ip 
# 2 test cases 
# 10 k 
# 2 3 5 1 9  arr 
# 3 [2, 3, 5] op

# 15 k 
# 5 5 5 20 arr 
# 3 [5, 5, 5] op
