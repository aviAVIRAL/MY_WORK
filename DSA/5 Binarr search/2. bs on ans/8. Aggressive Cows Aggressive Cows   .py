# Aggressive Cows : Detailed Solution
# Problem Statement: You are given an array ‘arr’ of size ‘n’ which denotes the position of stalls.
# You are also given an integer ‘k’ which denotes the number of aggressive cows.
# You are given the task of assigning stalls to ‘k’ cows such that the minimum distance between any two of them is the maximum possible.
# Find the maximum possible minimum distance.

# Examples
# Example 1:
# Input Format: N = 6, k = 4, arr[] = {0,3,4,7,10,9}
# Result: 3
# Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

# Example 2:
# Input Format: N = 5, k = 2, arr[] = {4,2,1,3,6}
# Result: 5
# Explanation: The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions {1, 6}. 


# brute

def canWePlace(stalls, dist, cows):
    n = len(stalls)  # size of array
    cntCows = 1  # no. of cows placed
    last = stalls[0]  # position of last placed cow
    for i in range(1, n):
        if stalls[i] - last >= dist:
            cntCows += 1  # place next cow
            last = stalls[i]  # update the last location
        if cntCows >= cows:
            return True
    return False

def aggressiveCows(stalls, k):
    n = len(stalls)  # size of array
    stalls.sort()  # sort the stalls[]
    limit = stalls[n - 1] - stalls[0]
    for i in range(1, limit + 1):
        if not canWePlace(stalls, i, k):
            return i - 1
    return limit

stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressiveCows(stalls, k)
print("The maximum possible minimum distance is:", ans)


# optimal 

def canWePlace(stalls, dist, cows):
    n = len(stalls)  # size of array
    cntCows = 1  # no. of cows placed
    last = stalls[0]  # position of last placed cow
    for i in range(1, n):
        if stalls[i] - last >= dist:
            cntCows += 1  # place next cow
            last = stalls[i]  # update the last location
        if cntCows >= cows:
            return True
    return False

def aggressiveCows(stalls, k):
    n = len(stalls)  # size of array
    stalls.sort()  # sort the stalls

    low = 1   
    high = stalls[n - 1] - stalls[0] #max(stalls) - min(salls)
    # apply binary search
    while low <= high:
        mid = (low + high) // 2
        if canWePlace(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high

stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressiveCows(stalls, k)
print("The maximum possible minimum distance is:", ans)








