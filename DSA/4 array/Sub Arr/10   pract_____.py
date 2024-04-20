
def f(arr, k):
    n = len(arr)  # size of the array.
    mp = {}
    sum = 0
    MaxiLen = 0
    
    cnt  = 0 
    for i in range(n):

        sum += arr[i]

        if sum == k:
            cnt += 1
            MaxiLen = max(MaxiLen, i + 1)

        rem = sum - k
        if rem in mp:
            length = i - mp[rem]
            MaxiLen = max(MaxiLen, length)

        if sum not in mp:  #edge case for zeros 
            mp[sum] = i

    return MaxiLen, cnt 

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

from collections import defaultdict

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1 # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt


if __name__ == '__main__':
    arr = [2,3,5 , 1, 9]
    k = 10
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)

