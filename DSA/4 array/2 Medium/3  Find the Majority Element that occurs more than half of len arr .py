

# Find the Majority Element that occurs more than N/2 times

# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.

# Examples
# Example 1:
# Input Format: N = 3, nums[] = {3,2,3}
# Result: 3
# Explanation: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 

# Example 2:
# Input Format:  N = 7, nums[] = {2,2,1,1,1,2,2}

# Result: 2

# Explanation: After counting the number of times each element appears and comparing it with half of array size, we get 2 as result.

# Example 3:
# Input Format:  N = 10, nums[] = {4,4,2,4,3,4,4,3,2,4}

# Result: 4




# brute  tc = O(N^2) sc = O(1)

def majorityElement(arr):
    n = len(arr)

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j] == arr[i]:
                cnt += 1

        # Check if frequency is greater than n/2
        if cnt > (n // 2):
            return arr[i]

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)



# better  mapping   

# Time Complexity: O(N*logN) + O(N), where N = size of the given array.
# Reason: We are using a map data structure. Insertion in the map takes logN time. And we are doing it for N elements. So, it results in the first term O(N*logN). The second O(N) is for checking which element occurs more than floor(N/2) times. If we use unordered_map instead, the first term will be O(N) for the best and average case and for the worst case, it will be O(N2).

# Space Complexity: O(N) as we are using a map data structure.

def f( arr ):
    n = len(arr)
    # ans  = n / 2

    mp = {}
    for x in arr : 
        if x not in mp : 
            mp[x] = 1
        else :
            mp[x] += 1 
 
    maxi = 0 
    for x in mp : 
        if mp[x] > n/2 :
            maxi = max(maxi, x )

    return maxi 

if __name__=="__main__": 
    arr =  [4,4,2,4,3,4,4,3,2,4]
    print(f(arr))

      
# better(same as mapping ) by  Import counting 
    
# Time Complexity: O(N*logN) + O(N), where N = size of the given array.
# Reason: We are using a map data structure. Insertion in the map takes logN time. And we are doing it for N elements. So, it results in the first term O(N*logN). The second O(N) is for checking which element occurs more than floor(N/2) times. If we use unordered_map instead, the first term will be O(N) for the best and average case and for the worst case, it will be O(N2).

# Space Complexity: O(N) as we are using a map data structure.


from collections import Counter

def majorityElement(arr):
    n = len(arr)

    # Count the occurrences of each element using Counter
    brr = Counter(arr)

    # Searching for the majority element
    for X, count in brr.items():
        if count > (n // 2):
            return X

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)


# optimal tc = 0(2n) sc = 0(1)  

def majorityElement(arr):
    n = len(arr)
    cnt = 0  # Count
    el = None  # Element

    # moores voting algo 
    for i in range(n):
        if cnt == 0:
            cnt = 1
            el = arr[i]
        elif el == arr[i]:
            cnt += 1
        else:
            cnt -= 1

    # verfication
    count = 0
    for i in range(n):
        if arr[i] == el:
            count += 1

    if count > (n / 2):
        return el
    return -1


arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)

# ....................

# concept   
arr = [100, 12, 999999, 999999, 2, 2, 1, 1, 1, 2, 9 ]
from collections import Counter
sol = Counter(arr)
print(sol) 
# op Counter({2: 3, 1: 3, 999999: 2 ,100: 1, 12: 1, 9: 1})
# indexing issue blunder : acc to cnt oder

# code  methoud using  liberary 
from collections import Counter

def majorityElement(arr):
    n = len(arr)
    sol = Counter(arr)

    for x, y in sol.items(): # same as mp 
        if y > (n // 2):
            return x

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)

print("............")

