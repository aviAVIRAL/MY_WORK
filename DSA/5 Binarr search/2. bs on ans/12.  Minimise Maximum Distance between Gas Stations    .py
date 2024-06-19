

# Minimise Maximum Distance between Gas Stations


# Problem Statement: You are given a sorted array ‘arr’ of length ‘n’, which contains positive integer positions of ‘n’ gas stations on the X-axis. You are also given an integer ‘k’. You have to place ‘k’ new gas stations on the X-axis. You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions. Let ‘dist’ be the maximum value of the distance between adjacent gas stations after adding k new gas stations.
# Find the minimum value of ‘dist’.

# Note: Answers within 10^-6 of the actual answer will be accepted. For example, if the actual answer is 0.65421678124, it is okay to return 0.654216. Our answer will be accepted if that is the same as the actual answer up to the 6th decimal place.

# Examples
# Example 1:
# Input Format: N = 5, arr[] = {1,2,3,4,5}, k = 4
# Result: 0.5
# Explanation: One of the possible ways to place 4 gas stations is {1,1.5,2,2.5,3,3.5,4,4.5,5}. Thus the maximum difference between adjacent gas stations is 0.5. Hence, the value of ‘dist’ is 0.5. It can be shown that there is no possible way to add 4 gas stations in such a way that the value of ‘dist’ is lower than this. 
# Example 2:
# Input Format: N = 10, arr[] = {1,2,3,4,5,6,7,8,9,10}, k = 1
# Result: 1
# Explanation: One of the possible ways to place 1 gas station is {1,1.5,2,3,4,5,6,7,8,9,10}. Thus the maximum difference between adjacent gas stations is still 1. Hence, the value of ‘dist’ is 1. It can be shown that there is no possible way to add 1 gas station in such a way that the value of ‘dist’ is lower than this. 


# brute 

def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of array
    howMany = [0] * (n - 1)

    # Pick and place k gas stations:      i m p
    for gasStations in range(1, k + 1): # for _ in range(k):

        # Find the maximum section and insert the gas station:
        maxSection = -1
        maxInd = -1
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            sectionLength = diff / (howMany[i] + 1)
            if sectionLength > maxSection:
                maxSection = sectionLength
                maxInd = i
        # insert the current gas station:
        howMany[maxInd] += 1

    # Find the maximum distance i.e. the answer:
    maxAns = -1
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        sectionLength = diff / (howMany[i] + 1)
        maxAns = max(maxAns, sectionLength)
    return maxAns

arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)

arr = [1, 13, 17, 23]
k = 5
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)

# Better

import heapq

def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of array.
    howMany = [0] * (n - 1)
    pq = []

    # insert the first n-1 elements into pq
    # with respective distance values:
    for i in range(n - 1):
        heapq.heappush(pq, ((-1)*(arr[i + 1] - arr[i]), i))

    # Pick and place k gas stations:
    for gasStations in range(1, k + 1):
        # Find the maximum section
        # and insert the gas station:
        tp = heapq.heappop(pq)
        secInd = tp[1]

        # insert the current gas station:
        howMany[secInd] += 1

        inidiff = arr[secInd + 1] - arr[secInd]
        newSecLen = inidiff / (howMany[secInd] + 1)
        heapq.heappush(pq, (newSecLen*(-1), secInd))

    return pq[0][0]*(-1)

arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)

# represenation 

import heapq

def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of array.
    howMany = [0] * (n - 1)
    pq = []

    for i in range(n - 1):
        heapq.heappush(pq, ((-1)*(arr[i + 1] - arr[i]), i))

# i m p
    for _ in range(k):
        tp = heapq.heappop(pq)
        secInd = tp[1]

        howMany[secInd] += 1

        inidiff = arr[secInd + 1] - arr[secInd]
        newSecLen = inidiff / (howMany[secInd] + 1)
        heapq.heappush(pq, ((-1)*newSecLen, secInd))

# i m p
    return heapq.heappop(pq)[0] * (-1)  # Return the maximum distance
    # return pq[0][0]*(-1)

arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)



arr = [1, 13, 17, 23]
k = 5
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)


# optimal 

def numberOfGasStationsRequired(dist, arr):
    n = len(arr)  # size of the array
    cnt = 0
    for i in range(1, n):
        numberInBetween = ((arr[i] - arr[i - 1]) / dist)
        if (arr[i] - arr[i - 1]) == (dist * numberInBetween):
            numberInBetween -= 1
        cnt += numberInBetween
    return cnt


def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of the array
    low = 0
    high = 0

    # Find the maximum distance:
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    # Apply Binary search:
    diff = 1e-6
    while high - low > diff:
        mid = (low + high) / 2.0
        cnt = numberOfGasStationsRequired(mid, arr)
        if cnt > k:
            low = mid
        else:
            high = mid

    return high


arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)





