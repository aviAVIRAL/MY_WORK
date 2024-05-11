
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
            subarrays.append(arr[mp[sum - k] + 1 : i+1])
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





