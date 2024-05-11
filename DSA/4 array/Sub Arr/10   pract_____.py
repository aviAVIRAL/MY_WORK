# .......................................
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


print()


def f(arr, k):
    n = len(arr)  # size of the array.
    mp = {}
    sum = 0
    subarrays = []

    for i in range(n):
        sum += arr[i]
        if sum == k:
            subarrays.append(arr[:i + 1])
        if sum - k in mp:
            subarrays.append(arr[mp[sum - k] + 1:i + 1])
        if sum not in mp:  # edge case for zeros 
            mp[sum] = i

    return subarrays

if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    result = f(arr, k)
    print("Subarrays with sum equal to", k, "are:")
    for subarray in result:
        print(subarray)








